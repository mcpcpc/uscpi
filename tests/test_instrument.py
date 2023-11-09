#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import IsolatedAsyncioTestCase
from unittest import main
from unittest.mock import AsyncMock
from unittest.mock import Mock
from unittest.mock import patch

from uscpi.instrument import Instrument


@patch("uscpi.instrument.ProtocolBase")
class TestInstrument(IsolatedAsyncioTestCase):
    async def test_cls(self, mock_protocol_base):
        mock_protocol_base.write = AsyncMock()
        instrument = Instrument(mock_protocol_base)
        await instrument.cls()
        mock_protocol_base.write.assert_awaited()

    async def test_ese_write_readline(self, mock_protocol_base):
        mock_protocol_base.write_readline = AsyncMock()
        mock_protocol_base.write_readline.return_value = b"test"
        instrument = Instrument(mock_protocol_base)
        self.assertEqual(await instrument.ese(), b"test")

    async def test_ese_write(self, mock_protocol_base):
        mock_protocol_base.write = AsyncMock()
        instrument = Instrument(mock_protocol_base)
        await instrument.ese(128)
        mock_protocol_base.write.assert_awaited()

    async def test_esr(self, mock_protocol_base):
        mock_protocol_base.write_readline = AsyncMock()
        mock_protocol_base.write_readline.return_value = b"test"
        instrument = Instrument(mock_protocol_base)
        self.assertEqual(await instrument.esr(), b"test")

    async def test_idn(self, mock_protocol_base):
        mock_protocol_base.write_readline = AsyncMock()
        mock_protocol_base.write_readline.return_value = b"test"
        instrument = Instrument(mock_protocol_base)
        self.assertEqual(await instrument.idn(), b"test")

    async def test_opc_write_readline(self, mock_protocol_base):
        mock_protocol_base.write_readline = AsyncMock()
        mock_protocol_base.write_readline.return_value = b"test"
        instrument = Instrument(mock_protocol_base)
        self.assertEqual(await instrument.opc(), b"test")

    async def test_opc_write(self, mock_protocol_base):
        mock_protocol_base.write = AsyncMock()
        instrument = Instrument(mock_protocol_base)
        await instrument.opc(complete=True)
        mock_protocol_base.write.assert_awaited()

    async def test_rst(self, mock_protocol_base):
        mock_protocol_base.write = AsyncMock()
        instrument = Instrument(mock_protocol_base)
        await instrument.rst()
        mock_protocol_base.write.assert_awaited()

    async def test_sre_write_readline(self, mock_protocol_base):
        mock_protocol_base.write_readline = AsyncMock()
        mock_protocol_base.write_readline.return_value = b"test"
        instrument = Instrument(mock_protocol_base)
        self.assertEqual(await instrument.sre(), b"test")

    async def test_sre_write(self, mock_protocol_base):
        mock_protocol_base.write = AsyncMock()
        instrument = Instrument(mock_protocol_base)
        await instrument.sre(value=128)
        mock_protocol_base.write.assert_awaited()

    async def test_stb(self, mock_protocol_base):
        mock_protocol_base.write_readline = AsyncMock()
        mock_protocol_base.write_readline.return_value = b"test"
        instrument = Instrument(mock_protocol_base)
        self.assertEqual(await instrument.stb(), b"test")

    async def test_trg(self, mock_protocol_base):
        mock_protocol_base.write = AsyncMock()
        instrument = Instrument(mock_protocol_base)
        await instrument.trg()
        mock_protocol_base.write.assert_awaited()

    async def test_tst(self, mock_protocol_base):
        mock_protocol_base.write_readline = AsyncMock()
        mock_protocol_base.write_readline.return_value = b"test"
        instrument = Instrument(mock_protocol_base)
        self.assertEqual(await instrument.tst(), b"test")

    async def test_wai(self, mock_protocol_base):
        mock_protocol_base.write = AsyncMock()
        instrument = Instrument(mock_protocol_base)
        await instrument.wai()
        mock_protocol_base.write.assert_awaited()


if __name__ == "__main__":
    main()
