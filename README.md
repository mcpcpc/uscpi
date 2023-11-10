# &mu;SCPI

An asynchronous SCPI instrumentation library.

## Install

### PyPI

Installing the latest release from [PyPI](https://pypi.org).

```console
pip install -U uscpi
```

### Repository

When using [git](https://git-scm.com), clone the repository and change your present working directory.

```console
git clone http://github.com/mcpcpc/uscpi
cd uscpi/
```

Create and activate a virtual environment.

```console
python3 -m venv venv
source venv/bin/activate
```

Install &mu;SCPI to the virtual environment.

```console
pip install -e .
```

## Usage

### Asynchronous

A basic example using the *asyncio* library.

```python
from asyncio import run
from uscpi.client import TCP
from uscpi.instrument import Instrument

client = TCP(host="127.0.0.1", port=5025)
instrument = Instrument(client=client)

async def main():
    response = await instrument.idn()
    print(response)

if __name__ == "__main__":
     run(main())
```

### Connection Timeout

By default, &mu;SCPI will wait indefinitely for a connection to be established. If the `timeout` property is defined, an *asyncio.TimeoutError* will be raised after the specified connection time period (in seconds) is exceeded.

```python
TCP(host="127.0.0.1", port=5025, timeout=0.1)
```

## Features

&mu;SCPI is fairly lightweight and leaves a majority of instrument function commands to be implemented by the user. Nonetheless, the following IEEE-488.2 commands have been implemented:

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

You can learn more about each of these commands by using the built-in `help` method.

```pycon
>>> from uscpi.instrument import Instrument
>>> help(Instrument)
```

## Credits

- [sockio](https://github.com/tiagocoutinho/sockio)
- [IEEE 488.2 Common Commands](https://rfmw.em.keysight.com/spdhelpfiles/truevolt/webhelp/US/Content/__I_SCPI/IEEE-488_Common_Commands.htm)
