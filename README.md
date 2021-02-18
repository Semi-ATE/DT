# Semi-ATE's Date & Time library

[![GitHub](https://img.shields.io/github/license/Semi-ATE/DT?color=black)](https://github.com/Semi-ATE/DT/blob/main/LICENSE)
[![Conda](https://img.shields.io/conda/pn/conda-forge/Semi-ATE-DT?color=black)](https://anaconda.org/conda-forge/Semi-ATE-DT)
![Supported Python versions](https://img.shields.io/badge/python-%3E%3D3.7-black)

[![CI](https://github.com/Semi-ATE/DT/workflows/CI/badge.svg?branch=main)](https://github.com/Semi-ATE/DT/actions?query=workflow%3ACI)
[![codecov](https://codecov.io/gh/Semi-ATE/DT/branch/main/graph/badge.svg?token=BAP0H9OMED)](https://codecov.io/gh/Semi-ATE/DT)
[![CD](https://github.com/Semi-ATE/DT/workflows/CD/badge.svg)](https://github.com/Semi-ATE/DT/actions?query=workflow%3ACD)

[![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/Semi-ATE/DT?color=blue&label=GitHub&sort=semver)](https://github.com/Semi-ATE/DT/releases/latest)
[![PyPI](https://img.shields.io/pypi/v/Semi-ATE-DT?color=blue&label=PyPI)](https://pypi.org/project/Semi-ATE-DT/)
![Conda (channel only)](https://img.shields.io/conda/vn/conda-forge/Semi-ATE-DT?color=blue&label=conda-forge)

# Installation

## Stand alone

### conda

```bash
$ conda install Semi-ATE-DT
```

### pip

```bash
$ pip install Semi-ATE-DT
```

## As part of the Semi-ATE suit

### conda (preferred)

```bash
$ conda install Semi-ATE
```

### pip ([discouraged](https://www.youtube.com/watch?v=Ul79ihg41Rs&t=2s) as Semi-ATE holds a plugin for [Spyder](https://github.com/spyder-ide/spyder))

```bash
$ pip install Semi-ATE
```

# Usage examples

```python
from Semi_ATE.DT import DT, TD

now = DT()
print(f"UTC time = {now}")
print(f"local time = {DT(now.local()}")
print(f"timezone = {now.tz}")  
print(f"daylight savings time = {now.dst}")
bow = DT(now.bow())
print(f"begin of week = {bow}")
eow = DT(now.eow()
print(f"end of week = {eow}")
bod = DT(now.bod())
print(f"begin of day = {bod}")
eod = DT(now.eod()
print(f"end of day = {eod}")



```



