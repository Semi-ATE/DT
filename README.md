# Semi-ATE's Time & Date library

[![GitHub](https://img.shields.io/github/license/Semi-ATE/TnD?color=black)](https://github.com/Semi-ATE/TnD/blob/main/LICENSE)
[![Conda](https://img.shields.io/conda/pn/conda-forge/Semi-ATE-TnD?color=black)](https://anaconda.org/conda-forge/Semi-ATE-TnD)
![Supported Python versions](https://img.shields.io/badge/python-%3E%3D3.7-black)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

[![CI](https://github.com/Semi-ATE/TnD/workflows/CI/badge.svg?branch=main)](https://github.com/Semi-ATE/TnD/actions?query=workflow%3ACI)
[![codecov](https://codecov.io/gh/Semi-ATE/TnD/branch/main/graph/badge.svg?token=BAP0H9OMED)](https://codecov.io/gh/Semi-ATE/TnD)
[![CD](https://github.com/Semi-ATE/TnD/workflows/CD/badge.svg)](https://github.com/Semi-ATE/TnD/actions?query=workflow%3ACD)

[![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/Semi-ATE/TnD?color=blue&label=GitHub&sort=semver)](https://github.com/Semi-ATE/TnD/releases/latest)
[![GitHub commits since latest release (by date)](https://img.shields.io/github/commits-since/Semi-ATE/TnD/latest)](https://github.com/Semi-ATE/TnD)
[![PyPI](https://img.shields.io/pypi/v/Semi-ATE-TnD?color=blue&label=PyPI)](https://pypi.org/project/Semi-ATE-TnD/)
![Conda (channel only)](https://img.shields.io/conda/vn/conda-forge/Semi-ATE-TnD?color=blue&label=conda-forge)

[![GitHub issues](https://img.shields.io/github/issues/Semi-ATE/TnD)](https://github.com/Semi-ATE/TnD/issues)
[![GitHub pull requests](https://img.shields.io/github/issues-pr/Semi-ATE/TnD)](https://github.com/Semi-ATE/TnD/pulls)

A library to easily navigate kalendars and have usefull information like quarter, datecode, kalendar week ...

# Installation

## Stand alone

### conda

```bash
$ conda install Semi-ATE-TnD
```

### pip

```bash
$ pip install Semi-ATE-TnD
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

The DT (Date and Time) object is used to navigate the calendar, determine kalendar-Week/Quarter/DateCode/...

```
Python 3.8.6 | packaged by conda-forge | (default, Jan 25 2021, 23:21:18) 
Type "copyright", "credits" or "license" for more information.

IPython 7.20.0 -- An enhanced Interactive Python.

In [1]: from Semi_ATE.TnD import DT

In [2]: now = DT()

In [3]: print(now)
Friday, February 19 2021 @ 10:28:07 (Q1 21075)

In [4]: print(f"We are now in KW{now.KW} Q{now.quarter}/{now.year}")
We are now in KW7 Q1/2021 

In [5]: print(f"Today's DateCode is '{now.datecode}'")
Today's DateCode is '21075'
```

### DT initialization & call

The DT object can be initialized the following ways:

- with no arguments : The DT object will be initialized with the Time and Date of your local machine (including day light savings and time-zone settings)
- with a date string "DDMMYYYY" : The DT object will be initialized by taking the beginning of this date.
- with a datecode string "YYWWD" : The DT object will be initialized by taking the beginning of the date indicated by the datecode.
- With an integer or float : The DT object will be initialized to the epoch number supplied.

We can also call the DT object in one of the above ways to re-initialize the object.

```
Python 3.8.6 | packaged by conda-forge | (default, Jan 25 2021, 23:21:18) 
Type "copyright", "credits" or "license" for more information.

IPython 7.20.0 -- An enhanced Interactive Python.

In [1]: from Semi_ATE.TnD import DT

In [2] start_of_school = DT("01092020")

In [3]: print(start_of_school)
Tuesday, September 1 2020 @ 00:00:00 (Q3 20362)

In[4]: who_am_i = DT("20075")

In[5]: print(who_am_i)
Friday, February 14 2020 @ 00:00:00 (Q1 20075)

In[6]: who_am_i(1000197990)

In[7]: print(who_am_i)
Tuesday, September 11 2001 @ 08:46:30 (Q3 01372)
```
### DT attributes

The DT object has the following attributes:

- datecode : string with the datecode "YYWWD"
- hour : integer indicating the hour
- min : integer indicating the minutes
- sec : integer indicating the seconds
- qhour : integer that indicates the quarter-hour
- wday : integer indicating the day of the week
- wday_name : string with the name of the day (english)
- mday : integer indicating the day of the month
- yday : integer indicating the day of the year
- KW : integer indicating the kalendar week [1..52/53]
- month : integer indicating the month [1..12]
- month_name : string with the month name (english)
- quarter : integer indicating the quarter
- year : integer inicating the year
- datetime : a datetime.datetime object
- date : string indicating the date "DDMMYYYY" 
- time : string indicating the time "HH:MM:SS"
- utc_offset : integer indicating offset from UTC in seconds 
- tz : integer indicating the time zone
- dst : integer indicating the current dayligt saving

Note: setting the attributes doesn't update the underlaying epoch yet (needs adding)

### DT methodes

the DT object has the following methods:

- boh() : sets the epoch to the beginning of the current hour
- eoh() : sets the epoch to the end of the current hour
- bod() : sets the epoch to the beginning of the current day
- eod() : sets the epoch to the end of the current day
- bow() : sets the epoch to the beginning of the current week
- eow() : sets the epoch to the end of the current week
- bom() : sets the epoch to the beginning of the current month
- eom() : sets the epoch to the end of the current month
- boy() : sets the epoch to the beginning of the current year
- eoy() : sets the epoch to the end of the current year
- local() : returns the epoch but in local terms

#### note: negative epoch 

The epoch (1 January 1970 00:00:00 UTC) is basically just a `marker` from where to count the number of seconds from.

If one wants to reference a point in time before the epoch, one uses negative epoch numbers. This works fine on Linux (and MacOS?) but as usual Windows has another opinion, so negative epoch times can't be used on Windows machines. :unamused:

[One of our issues addresses this](https://github.com/Semi-ATE/DT/issues/4), and we'll see if we can fix this :stuck_out_tongue:

### Operator overloading

Currently only `DT - DT = TD` (see below) is implemented, planned additions :

- `+int`, `int+`, `+=int`, 
- `-int`, `int-`, `-=int` 
- `+floar`, `float+`, `+=float` 
- `-float`, `float-`, `-=float`
- `DT+TD`, `TD+DT`, `+=DT`
- `DT-TD`, `TD-DT`, `-=DT`

## The TD object 

The TD (Time Difference) is the result of the substraction of two DT objects.

```
Python 3.8.6 | packaged by conda-forge | (default, Jan 25 2021, 23:21:18) 
Type "copyright", "credits" or "license" for more information.

IPython 7.20.0 -- An enhanced Interactive Python.

In [1]: from Semi_ATE.TnD import DT, TD

In [2]: now = DT()

In [3]: my_birth_day = DT("01101982")  # DDMMYYYY

In [4]: my_age = now - my_birth_day

In [5]: print(my_age)
38 years 4 months 4 weeks 1 day 18 hours 28 minutes 7 seconds

```

## Chronometer

The Chronometer class has the followint methods

- `reset()` : Resets and arms the chronometer for a next run
- `start()` : stars the chronometer (with lap #1)
- `stop()` : stops the chronometer
- `lap()` : starts the next lap
- `laps()` : returns the number of laps recorded
- `time()` : returns the total time of all laps
- `laptimes()` : returns a list of floats, each is the laptime of the corresponding index
- `averagelaptime()` : the average lap time

## Interact with Qt

It was elected **not** to incorporate the binding to Qt in this library, so that we can also work with this library without the precense of Qt.

It is however easy enough to bind the two as shown below

```
Python 3.8.6 | packaged by conda-forge | (default, Jan 25 2021, 23:21:18) 
Type "copyright", "credits" or "license" for more information.

IPython 7.20.0 -- An enhanced Interactive Python.

In [1]: from Semi_ATE.DT import DT

In [2]: from PyQt5.QtCore import QDateTime

In [3]: here_and_now = DT()

In [4]: QtHereAndNow = QDateTime()

In [5]: QtHereAndNow.setOffsetFromUtc(here_and_now.utc_offset)  # account for timezone + day light saving

In [6]: QtHereAndNow.setSecsSinceEpoch(here_and_now.epoch)

```

from QDateTime you can go to QDate and QTime if you so desire, or you do something similar as above.
