#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase
from unittest import main
from unittest.mock import Mock

from uscpi.protocol import CallbackProtocol


class TestProtocol(TestCase):
    def setUp(self):
        self.srp = CallbackProtocol(Mock(), loop=Mock())

    def test_callback_protocol_connection_made_cb(self):
        self.srp.connection_made_cb = Mock()
        self.srp.connection_made(transport=Mock())
        self.srp.connection_made_cb.assert_called_once()

    def test_callback_protocol_connection_lost_cb(self):
        self.srp.connection_lost_cb = Mock()
        self.srp.connection_lost(exc=Mock())
        self.srp.connection_lost_cb.assert_called_once()

    def test_callback_protocol_data_received_cb(self):
        self.srp.data_received_cb = Mock()
        self.srp.data_received(data=Mock())
        self.srp.data_received_cb.assert_called_once()

    def test_callback_protocol_eof_received_cb(self):
        self.srp.eof_received_cb = Mock()
        self.srp.eof_received()
        self.srp.eof_received_cb.assert_called_once()


if __name__ == "__main__":
    main()
