# NetOI-check
CLI for submitting problem solutions to [NetOI](https://netoi.org.ua).

## Installation

This module is Python 2/3 compatible so, you can use
[pip](https://pypi.python.org/pypi/pip) for one of these versions.

```(shell)
$ pip install netoi-check
```

## How to use

```(shell)
usage: netoi-check [-h] --problem PROBLEM --source SOURCE
                   [--language {cpp,java,py3,pas}] [--silent] [--html HTML]

Send problem to check

optional arguments:
  -h, --help            show this help message and exit
  --problem PROBLEM, -p PROBLEM
                        Problem name
  --source SOURCE, -s SOURCE
                        Source to check
  --language {cpp,java,py3,pas}, -l {cpp,java,py3,pas}
                        Specify programming language
  --silent              Silent mode
  --html HTML           Save results in html
```

## License

MIT
