#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import IsolatedAsyncioTestCase
from unittest import main
from unittest.mock import AsyncMock
from unittest.mock import Mock
from unittest.mock import patch

from uscpi.protocol import TCP


@patch("uscpi.protocol.open_connection")
class TestTCP(IsolatedAsyncioTestCase):
    def setUp(self):
        self.tcp = TCP("127.0.0.1", 8080)
        self.mock_reader = AsyncMock()
        self.mock_writer = AsyncMock()
        self.mock_writer.drain = AsyncMock()
        self.mock_writer.write = Mock()

    async def test_tcp_open(self, mock_open_connection):
        mock_open_connection.return_value = self.mock_reader, self.mock_writer
        await self.tcp.open()
        mock_open_connection.assert_called_once_with("127.0.0.1", 8080)
        self.assertIsNotNone(self.tcp.reader)
        self.assertIsNotNone(self.tcp.writer)

    async def test_tcp_close(self, mock_open_connection):
        self.tcp.reader = self.mock_reader
        self.tcp.writer = self.mock_writer
        await self.tcp.close()
        self.assertIsNone(self.tcp.reader)
        self.assertIsNone(self.tcp.writer)

    async def test_tcp_readline(self, mock_open_connection):
        mock_open_connection.return_value = self.mock_reader, self.mock_writer
        self.mock_reader.readline.return_value = b"test\n"
        self.assertEqual(await self.tcp.readline(), b"test\n")

    async def test_tcp_readuntil(self, mock_open_connection):
        mock_open_connection.return_value = self.mock_reader, self.mock_writer
        self.mock_reader.readuntil.return_value = b"test\n"
        self.assertEqual(await self.tcp.readuntil(b"\n"), b"test\n")

    async def test_tcp_write(self, mock_open_connection):
        mock_open_connection.return_value = self.mock_reader, self.mock_writer
        await self.tcp.write(b"test\n")
        self.mock_writer.drain.assert_awaited()
        self.mock_writer.write.assert_called_with(b"test\n")

    async def test_tcp_write_readline(self, mock_open_connection):
        mock_open_connection.return_value = self.mock_reader, self.mock_writer
        self.mock_reader.readline.return_value = b"test\n"
        response = await self.tcp.write_readline(b"test\n")
        self.mock_writer.drain.assert_awaited()
        self.mock_writer.write.assert_called_with(b"test\n")
        self.assertEqual(response, b"test\n")


if __name__ == "__main__":
    main()
