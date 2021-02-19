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

[![GitHub issues](https://img.shields.io/github/issues/Semi-ATE/DT)](https://github.com/Semi-ATE/DT/issues)





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

# Usage & examples

## The DT object

The DT (Date and Time) is used to navigate the calendar

```python
Python 3.8.6 | packaged by conda-forge | (default, Jan 25 2021, 23:21:18) 
Type "copyright", "credits" or "license" for more information.

IPython 7.20.0 -- An enhanced Interactive Python.

In [1]: from Semi_ATE.TnD import DT

In [2]: now = DT()

In [3]: print(now)
Friday, February 19 2021 @ 10:28:07 (Q1 21075)

```
### DT initialization & call

### DT attributes

### DT methodes

## The TD object 

The TD (Time Difference) is the result of the substraction of two DT objects.

```python
Python 3.8.6 | packaged by conda-forge | (default, Jan 25 2021, 23:21:18) 
Type "copyright", "credits" or "license" for more information.

IPython 7.20.0 -- An enhanced Interactive Python.

In [1]: from Semi_ATE.TnD import DT, TD

In [2]: now = DT()

In [3]: my_birth_day = DT("01101982")

In [4]: my_age = now - my_birth_day

In [5]: print(my_age)
38 years 4 months 4 weeks 1 day 18 hours 28 minutes 7 seconds

```

## Chronometer



## Interact with Qt

It was elected not to incorporate the binding to Qt in this library, so that we can also work with this library without the precense of Qt.
It is however easy enough to bind the two as shown below

```python
Python 3.8.6 | packaged by conda-forge | (default, Jan 25 2021, 23:21:18) 
Type "copyright", "credits" or "license" for more information.

IPython 7.20.0 -- An enhanced Interactive Python.

In [1]: from Semi_ATE.TnD import DT

In [2]: from PyQt5.QtCore import QDateTime

In [3]: here_and_now = DT()

In [4]: QtHereAndNow = QDateTime()

In [5]: QtHereAndNow.setOffsetFromUtc(here_and_now.utc_offset)  # account for timezone + day light saving

In [6]: QtHereAndNow.setSecsSinceEpoch(here_and_now.epoch)

```

from QDateTime you can go to QDate and QTime if you so desire, or you do something similar as above.
