#!/usr/bin/env python
# -*- coding: utf-8 -*-

from asyncio import iscoroutine
from asyncio import StreamReaderProtocol
from typing import Callable


class CallbackProtocol(StreamReaderProtocol):
    """Callback protocol.

    A wrapper for StreamReaderProtocol that allows users to
    implement their own custom callback functions. Each user
    function will be called after to the
    StreamReaderProtocol helper method.
    """

    def _exec_callback(self, name: str, *args, **kwargs) -> None:
        callback = getattr(self, name, None)
        if callback is None:
            return
        result = callback(*args, **kwargs)
        if iscoroutine(result):
            self._loop.create_task(result)

    def connection_made(self, transport):
        result = super().connection_made(transport)
        self._exec_callback("connection_made_cb", transport)
        return result

    def connection_lost(self, exc):
        result = super().connection_lost(exc)
        self._exec_callback("connection_lost_cb", exc)
        return result

    def data_received(self, data):
        result = super().data_received(data)
        self._exec_callback("data_received_cb", data)
        return result

    def eof_received(self):
        result = super().eof_received()
        self._exec_callback("eof_received_cb")
        return result
