#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dataclasses import dataclass

from uscpi.protocol import ProtocolBase


@dataclass
class Instrument:
    """
    Instrument representation. Implements common commands
    associated with IEEE-488.2.
    """

    protocol: ProtocolBase

    def cls(self) -> None:
        """Clear Status Command.

        Clears the event registers in all register groups.
        Also clears the error queue.
        """

        return self.protocol.write(b"*CLS\n")

    def ese(self, value: int = None) -> bytes | None:
        """Event Status Enable Command and Query.

        Enables bits in the enable register for the Standard
        Event Register group. The selected bits are then
        reported to bit 5 of the Status Byte Register. An
        enable register defines which bits in the event
        register will be reported to the Status Byte
        register group. You can write to or read from an
        enable register.

        Args:
            value: An integer in the range of 0 through 255.

        Returns:
             If value is not specified, returns the content
             of the Standard Event Status Enable register.
        """

        if isinstance(value, int):
            if value not in range(256):
                raise ValueError(value)
            return self.protocol.write(f"*ESE {value}\n".encode())
        return self.protocol.write_readline(b"*ESE?\n")

    def esr(self) -> bytes:
        """Standard Event Status Register Query.

        Queries the event register for the Standard Event
        Register group.

        An event register is a read-only register that
        latches events from the condition register. While an
        event bit is set, subsequent events corresponding to
        that bit are ignored.
        """

        return self.protocol.write_readline(b"*ESR?\n")

    def idn(self) -> bytes:
        """Identification Query.

        Returns the instrument’s identification string.

        Returns:
            A string organized into four fields separated by
            commas.
        """

        return self.protocol.write_readline(b"*IDN?\n")

    def opc(self, complete: bool = False) -> bytes | None:
        """Operation Complete Command and Query.

        Sets "Operation Complete" (bit 0) in the Standard
        Event register at the completion of the current
        operation.
        """

        if isinstance(complete, bool) and complete:
            return self.protocol.write(b"*OPC\n")
        return self.protocol.write_readline(b"*OPC?\n")

    def rst(self) -> None:
        """Reset Command.

        Resets instrument to factory default state,
        independent of MMEMory:STATe:RECall:AUTO setting.
        This is similar to SYSTem:PRESet. The difference is
        that *RST resets the instrument for SCPI operation,
        and SYSTem:PRESet resets the instrument for
        front-panel operation. As a result, *RST turns the
        histogram and statistics off, and SYSTem:PRESet
        turns them on (CALC:TRAN:HIST:STAT ON).
        """

        return self.protocol.write(b"*RST\n")

    def sre(self, value: int = None) -> bytes | None:
        """Service Request Enable Command and Query.

        Service Request Enable. Enables bits in the enable
        register for the Status Byte Register group. An
        enable register defines which bits in the event
        register will be reported to the Status Byte
        register group. You can write to or read from an
        enable register.

        Args:
            value: An integer in the range of 0 through 255.

        Returns:
             If value is not specified, returns the content
             of the Service Request Enable register.
        """

        if isinstance(value, int):
            if value not in range(256):
                raise ValueError(value)
            return self.protocol.write(f"*SRE {value}\n".encode())
        return self.protocol.write_readline(b"*SRE?\n")

    def stb(self) -> bytes:
        """Read Status Byte Query.

        Queries the condition register for the Status Byte
        Register group and returns a decimal value equal to
        the binary-weighted sum of all bits set in the
        register.

        A condition register continuously monitors the state
        of the instrument. Condition register bits are
        updated in real time; they are neither latched nor
        buffered.

        Returns:
            The status byte and Master Summary Status bit.
        """

        return self.protocol.write_readline(b"*STB?\n")

    def trg(self) -> None:
        """Trigger Command.

        Triggers the instrument if TRIGger:SOURce BUS is
        selected.
        """

        return self.protocol.write("*TRG\n")

    def tst(self) -> bytes:
        """Self-Test Query.

        Performs a basic self-test of the instrument and
        returns a pass/fail indication. The TEST:ALL?
        self-test is more comprehensive than the *TST?
        self-test.

        Returns:
            An integer value in the range of -32767 and
            32767. A response of 0 indicates that the
            self-test completed without errors detected.
        """

        return self.protocol.write_readline(b"*TST?\n")

    def wai(self) -> None:
        """Wait-to-Continue Command.

        Configures the instrument's output buffer to wait
        for all pending operations to complete before
        executing any additional commands over the
        interface.
        """

        return self.protocol.write(b"*WAI\n")
