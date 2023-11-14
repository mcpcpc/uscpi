#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abc import ABC
from abc import abstractmethod
from asyncio import get_running_loop
from asyncio import Lock
from asyncio import StreamReader
from asyncio import StreamReaderProtocol
from asyncio import StreamWriter
from asyncio import wait_for
from functools import wraps


async def open_connection(
    host: str = None, port: int = None, limit: int = 2**16, **kwargs
) -> tuple:
    """Open connection.

    Identical to the CPython helper method implementation
    but with optional callback arguments.
    """

    loop = get_running_loop()
    reader = StreamReader(limit=limit, loop=loop)
    protocol = StreamReaderProtocol(reader, loop=loop)
    transport, _ = await loop.create_connection(lambda: protocol, host, port, **kwargs)
    writer = StreamWriter(transport, protocol, reader, loop)
    return reader, writer


class ClientBase(ABC):
    """
    Client base representation.
    """

    @abstractmethod
    async def close(self, *args, **kwargs) -> None:
        ...

    @abstractmethod
    async def open(self, *args, **kwargs) -> None:
        ...


class TCP(ClientBase):
    """
    TCP client representation.
    """

    lock: Lock | None = None
    reader: StreamReader | None = None
    writer: StreamWriter | None = None

    def __init__(
        self, host: str, port: int, timeout: int | float | None = None
    ) -> None:
        self.host = host
        self.port = port
        self.timeout = timeout

    @staticmethod
    def connection(func):
        """
        Attempt to establish/re-establish connection.
        """

        @wraps(func)
        async def wrapper(self, *args, **kwargs):
            if not isinstance(self.lock, Lock):
                self.lock = Lock()
            async with self.lock:
                if not self.is_connected():
                    await self.open()
            coroutine = func(self, *args, **kwargs)
            return await coroutine

        return wrapper

    def is_eof(self) -> bool:
        """
        Check if EOF stream reader flag reached.
        """

        reader_exists = isinstance(self.reader, StreamReader)
        return reader_exists and self.reader.at_eof()

    def is_connected(self) -> bool:
        """
        Check if stream reader exists.
        """

        reader_exists = isinstance(self.reader, StreamReader)
        return reader_exists and not self.is_eof()

    async def close(self, *args, **kwargs) -> None:
        """
        Close active reader and writer streams.
        """

        if isinstance(self.writer, StreamWriter):
            self.writer.close()
            await self.writer.wait_closed()
        self.reader = None
        self.writer = None

    async def open(self, *args, **kwargs) -> None:
        """
        Open new reader and writer streams.
        """

        if self.is_connected():
            raise Exception("Already connected.")
        await self.close()
        coroutine = open_connection(self.host, self.port)
        if isinstance(self.timeout, (int, float)):
            coroutine = wait_for(coroutine, self.timeout)
        self.reader, self.writer = await coroutine

    @connection
    async def readline(self) -> bytes:
        """
        Read and return one line, where "line" is a sequence
        of bytes ending with \\n.
        """

        return await self.reader.readline()

    @connection
    async def readuntil(self, separator: bytes = b"\n") -> bytes:
        """
        Read and return data from the stream until separator
        is found.
        """

        return await self.reader.readuntil(separator)

    @connection
    async def write(self, data: bytes) -> None:
        try:
            self.writer.write(data)
            await self.writer.drain()
        except ConnectionError:
            await self.close()
            raise

    @connection
    async def write_readline(self, data: bytes) -> bytes:
        """
        Write a message string and immediately return line
        from stream.
        """

        try:
            self.writer.write(data)
            await self.writer.drain()
        except ConnectionError:
            await self.close()
            raise
        return await self.reader.readline()
