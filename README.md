# &mu;SCPI

An asynchronous SCPI instrumentation library.

## Installation

Installing the latest release from [PyPI](https://pypi.org).

```console
pip install -U uscpi
```

Installing from the latest source using [git](https://git-scm.com).

```console
git clone http://github.com/mcpcpc/uscpi
cd uscpi/
pip install .
```

## Usage

A basic example using the *asyncio* library.

```python
from asyncio import run
from uscpi.protocol import TCP
from uscpi.instrument import Instrument

protocol = TCP(host="127.0.0.1", port=5025)
instrument = Instrument(protocol=protocol)

async def main():
    response = await instrument.idn()
    print(response)

if __name__ == "__main__":
     run(main())
```

## Features

The `uscpi` is fairly lightweight and leaves a majority of instrument function commands to be implemented by the user. Nonetheless, the following IEEE-488.2 commands have been implemented:

- Clear Status Command
- Event Status Enable Command and Query
- Standard Event Status Register Query
- Identification Query
- Reset Command
- Service Request Enable Command and Query
- Read Status Byte Query
- Trigger Command
- Self-Test Query
- Wait-to-Continue Command

## Credits

- [sockio](https://github.com/tiagocoutinho/sockio)
- [IEEE 488.2 Common Commands](https://rfmw.em.keysight.com/spdhelpfiles/truevolt/webhelp/US/Content/__I_SCPI/IEEE-488_Common_Commands.htm)
