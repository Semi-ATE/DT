# Semi-ATE's STDF library

**STDF** stands for **S**tandard **T**est **D**ata **F**ormat

[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/Semi-ATE/STDF/blob/main/LICENSE)
![Python >= 3.7](https://img.shields.io/badge/Python-%3E%3D3.7-blue)
[![CI](https://github.com/Semi-ATE/STDF/workflows/CI/badge.svg?branch=main)](https://github.com/Semi-ATE/STDF/actions?query=workflow%3ACI)
[![codecov](https://codecov.io/gh/Semi-ATE/STDF/branch/main/graph/badge.svg?token=BAP0H9OMED)](https://codecov.io/gh/Semi-ATE/STDF)
[![CD](https://github.com/Semi-ATE/STDF/workflows/CD/badge.svg)](https://github.com/Semi-ATE/STDF/actions?query=workflow%3ACD)
[![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/Semi-ATE/STDF?color=blue&label=GitHub&sort=semver)](https://github.com/Semi-ATE/STDF/releases/latest)
[![PyPI](https://img.shields.io/pypi/v/Semi-ATE-STDF?color=blue&label=PyPI)](https://pypi.org/project/Semi-ATE-STDF/)
![Conda (channel only)](https://img.shields.io/conda/vn/conda-forge/Semi-ATE-STDF?color=blue&label=conda-forge)





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
from Semi_ATE.DT import DT, DTD

now = DT()
print(f"UTC time = {now}")
print(f"local time = {DT(now.local()}")
print(f"timezone = {now.tz}")  
print(f"daylight savings time = {now.dst}")
print(f"begin of week = {DT(now.bow())}")
print(f"end of week = {DT(now.eow()}")
print(f"begin of day = {DT(now.bod()}")
print(f"end of day = {DT(now.eod()}")
```



