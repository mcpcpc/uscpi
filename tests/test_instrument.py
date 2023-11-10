#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import IsolatedAsyncioTestCase
from unittest import main
from unittest.mock import AsyncMock
from unittest.mock import Mock
from unittest.mock import patch

from uscpi.instrument import Instrument


@patch("uscpi.instrument.ClientBase")
class TestInstrument(IsolatedAsyncioTestCase):
    async def test_cls(self, mock_client_base):
        mock_client_base.write = AsyncMock()
        instrument = Instrument(mock_client_base)
        await instrument.cls()
        mock_client_base.write.assert_awaited()

    async def test_ese_write_readline(self, mock_client_base):
        mock_client_base.write_readline = AsyncMock()
        mock_client_base.write_readline.return_value = b"test"
        instrument = Instrument(mock_client_base)
        self.assertEqual(await instrument.ese(), b"test")

    async def test_ese_write(self, mock_client_base):
        mock_client_base.write = AsyncMock()
        instrument = Instrument(mock_client_base)
        await instrument.ese(128)
        mock_client_base.write.assert_awaited()

    async def test_esr(self, mock_client_base):
        mock_client_base.write_readline = AsyncMock()
        mock_client_base.write_readline.return_value = b"test"
        instrument = Instrument(mock_client_base)
        self.assertEqual(await instrument.esr(), b"test")

    async def test_idn(self, mock_client_base):
        mock_client_base.write_readline = AsyncMock()
        mock_client_base.write_readline.return_value = b"test"
        instrument = Instrument(mock_client_base)
        self.assertEqual(await instrument.idn(), b"test")

    async def test_opc_write_readline(self, mock_client_base):
        mock_client_base.write_readline = AsyncMock()
        mock_client_base.write_readline.return_value = b"test"
        instrument = Instrument(mock_client_base)
        self.assertEqual(await instrument.opc(), b"test")

    async def test_opc_write(self, mock_client_base):
        mock_client_base.write = AsyncMock()
        instrument = Instrument(mock_client_base)
        await instrument.opc(complete=True)
        mock_client_base.write.assert_awaited()

    async def test_rst(self, mock_client_base):
        mock_client_base.write = AsyncMock()
        instrument = Instrument(mock_client_base)
        await instrument.rst()
        mock_client_base.write.assert_awaited()

    async def test_sre_write_readline(self, mock_client_base):
        mock_client_base.write_readline = AsyncMock()
        mock_client_base.write_readline.return_value = b"test"
        instrument = Instrument(mock_client_base)
        self.assertEqual(await instrument.sre(), b"test")

    async def test_sre_write(self, mock_client_base):
        mock_client_base.write = AsyncMock()
        instrument = Instrument(mock_client_base)
        await instrument.sre(value=128)
        mock_client_base.write.assert_awaited()

    async def test_stb(self, mock_client_base):
        mock_client_base.write_readline = AsyncMock()
        mock_client_base.write_readline.return_value = b"test"
        instrument = Instrument(mock_client_base)
        self.assertEqual(await instrument.stb(), b"test")

    async def test_trg(self, mock_client_base):
        mock_client_base.write = AsyncMock()
        instrument = Instrument(mock_client_base)
        await instrument.trg()
        mock_client_base.write.assert_awaited()

    async def test_tst(self, mock_client_base):
        mock_client_base.write_readline = AsyncMock()
        mock_client_base.write_readline.return_value = b"test"
        instrument = Instrument(mock_client_base)
        self.assertEqual(await instrument.tst(), b"test")

    async def test_wai(self, mock_client_base):
        mock_client_base.write = AsyncMock()
        instrument = Instrument(mock_client_base)
        await instrument.wai()
        mock_client_base.write.assert_awaited()


if __name__ == "__main__":
    main()
