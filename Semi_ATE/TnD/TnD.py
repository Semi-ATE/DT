"""
Created on Jun 14, 2014

@author: $Author: tho $

This Library implements Date and Time manipulations in a convenient way.

License : MIT
"""
import datetime
import os
import time
import platform


def is_date(stamp):
    """
    This function will return True or False, depending if the supplied stamp
    can be interpreted as a date string of format DDMMYYYY
    """
    if isinstance(stamp, str):
        if len(stamp) == 8:
            if stamp.isdigit():
                DD = int(stamp[:2])
                if DD > 31:
                    return False
                MM = int(stamp[2:4])
                if MM > 12:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False
    return True


def is_datecode(stamp):
    """
    This function will return True or False, depending if the supplied stamp
    can be interpreted as a date-code string of the format YYWWD
    """
    if type(stamp) == str:
        if len(stamp) == 5:
            year = stamp[0:2]
            if not year.isdigit():
                return False
            week = stamp[2:4]
            if week.isdigit():
                week = int(week)
                if (week < 1) or (week > 53):
                    return False
            else:
                return False
            day = stamp[4]
            if day.isdigit():
                day = int(day)
                if (day < 1) or (day > 7):
                    return False
                else:
                    return True
            else:
                return False
        else:
            return False
    else:
        return False


def iso_year_start(iso_year):
    "The gregorian calendar date of the first day of the given ISO year"
    fourth_jan = datetime.date(iso_year, 1, 4)
    delta = datetime.timedelta(fourth_jan.isoweekday() - 1)
    return fourth_jan - delta


def iso_to_gregorian(iso_year, iso_week, iso_day):
    "Gregorian calendar date for the given ISO year, week and day"
    year_start = iso_year_start(iso_year)
    return year_start + datetime.timedelta(days=iso_day - 1, weeks=iso_week - 1)


def micronas_time_structure_to_epoch(Datum=0, Uhrzeit=0):
    """
    Micronas uses the following legacy structures:

    Datum : YYYYYYMM MMDDDDD0 (2 bytes)
                YYYYYY --> Year  6 bit, range = 0..63, offset is 2000
                MMMM ----> Month 4 bit, range = 0..15, 0=january .. 11=december
                DDDDD ---> Day   5 bit, range = 0..31, 0 is not used, 1=first day of the month and so on

    Uhrzeit : HHHHHHHH MMMMMMMM (2 bytes)
                HHHHHHHH --> Hour    8 bit, range = 0..255 only 0..23 is used
                MMMMMMMM --> Minutes 8 bit, range = 0..255 only 0..59 is used

    This function returns the seconds since epoch for the given Datum and Uhrzeit as an initializer for the DT objects
    """
    year = (Datum & (0b111111 << 10)) >> 10
    month = (Datum & (0b1111 << 6)) >> 6
    day_of_month = (Datum & (0b11111 << 1)) >> 1
    hours = (Uhrzeit & (0b11111111 << 8)) >> 8
    minutes = Uhrzeit & 0b11111111
    dt = DT("%2s%2s%4s" % (day_of_month, month + 1, year + 2000))
    return dt.epoch + (hours * 60 * 60) + (minutes * 60)


class DTError(RuntimeError):
    """
    module exception
    """

    def __init__(self, arg):
        self.args = arg


class TD(object):
    """
    Time Differnce Object
    """

    def __init__(self, diff):
        self.__call__(diff)

    def __call__(self, diff):
        self.diff = diff

    def seconds(self):
        return self.diff

    def minutes(self):
        return self.diff / 60

    def hours(self):
        return self.diff / (60 * 60)

    def days(self):
        return self.diff / (60 * 60 * 24)

    def weeks(self):
        return self.diff / (60 * 60 * 24 * 7)

    def months(self):
        return self.diff / (60 * 60 * 24 * 365 / 12)

    def years(self):
        return self.diff / (60 * 60 * 24 * 365)

    def __str__(self):
        """
        3 years 2 months 3 weeks 4 days 15 hours 20 mintes 3 seconds
        1 year 1 week 16 seconds
        2 minutes 1 second
        """
        retval = ""
        remainer = self.diff
        # years
        if remainer > (60 * 60 * 24 * 365):
            Years = int(remainer / (60 * 60 * 24 * 365))
            remainer -= Years * 60 * 60 * 24 * 365
            if Years == 1:
                retval += "1 year"
            else:
                retval += f"{Years} years"
        # months
        if remainer > (60 * 60 * 24 * 365) / 12:
            Months = int(remainer / ((60 * 60 * 24 * 365) / 12))
            remainer -= Months * ((60 * 60 * 24 * 365) / 12)
            if Months == 1:
                retval += " 1 month"
            else:
                retval += f" {Months} months"
        # weeks
        if remainer > (60 * 60 * 24 * 7):
            Weeks = int(remainer / (60 * 60 * 24 * 7))
            remainer -= Weeks * 60 * 60 * 24 * 7
            if Weeks == 1:
                retval += " 1 week"
            else:
                retval += f" {Weeks} weeks"
        # days
        if remainer > (60 * 60 * 24):
            Days = int(remainer / (60 * 60 * 24))
            remainer -= Days * 60 * 60 * 24
            if Days == 1:
                retval += " 1 day"
            else:
                retval += f" {Days} days"
        # hours
        if remainer > (60 * 60):
            Hours = int(remainer / (60 * 60))
            remainer -= Hours * 60 * 60
            if Hours == 1:
                retval += " 1 hour"
            else:
                retval += f" {Hours} hours"
        # minutes
        if remainer > 60:
            Minutes = int(remainer / 60)
            remainer -= Minutes * 60
            if Minutes == 1:
                retval += " 1 minute"
            else:
                retval += f" {Minutes} minutes"
        # seconds
        if remainer == 1:
            retval += " 1 second"
        else:
            retval += f" {int(remainer)} seconds"
        return retval.strip()


class DT(object):
    """
    Date and Time Object
    """

    def __init__(self, stamp=None):
        loct = int(time.time())
        self.tz = (time.mktime(time.gmtime(loct)) - loct) / 3600
        self.dst = time.localtime()[8]
        self.os = platform.system()
        self.__call__(stamp)

    def __call__(self, stamp=None):
        if stamp == None:
            self.epoch = int(time.time())
        elif isinstance(stamp, int) or isinstance(stamp, float):
            self.epoch = int(stamp)
        elif isinstance(stamp, str):
            if is_datecode(stamp):  # YYWWD
                # set epoch to the beginning of the datecode
                # http://stackoverflow.com/questions/5882405/get-date-from-iso-week-number-in-python
                iso_year = int(stamp[:2])
                if iso_year > 70:  # epoch = 1 Jan 1970 ;-)
                    iso_year += 1900
                else:
                    iso_year += 2000
                iso_week = int(stamp[2:4])
                iso_day = int(stamp[4])
                temp = iso_to_gregorian(iso_year, iso_week, iso_day)
                self.epoch = int(
                    (
                        datetime.datetime(temp.year, temp.month, temp.day)
                        - datetime.datetime(1970, 1, 1)
                    ).total_seconds()
                )
            elif is_date(stamp):  # DDMMYYYY
                DD = int(stamp[:2])
                MM = int(stamp[2:4])
                YYYY = int(stamp[4:])
                self.epoch = int(
                    (
                        datetime.datetime(YYYY, MM, DD) - datetime.datetime(1970, 1, 1)
                    ).total_seconds()
                )
            else:
                raise DTError(
                    f"can not interprete the string '{stamp}' as an initializer"
                )
        else:
            raise DTError("Don't now how to handle type(%s)=%s" % (stamp, type(stamp)))
        self._populate()

    def _populate(self):
        if self.os == "Windows" and self.epoch < -43200:
            raise DTError("Windows doesn't support negative epoch times beyond -43200 (12 hours prior)")
        t = time.gmtime(self.epoch)
        d = datetime.date(t.tm_year, t.tm_mon, t.tm_mday)
        self.datecode = "%4d%02d%1d" % (
            d.isocalendar()[0],
            d.isocalendar()[1],
            d.isocalendar()[2],
        )  # YYYYWWD
        self.datecode = self.datecode[2:]  # YYWWD
        self.min = t.tm_min  # minute of the hour [0 .. 59]
        if self.min < 15:
            self.qhour = 1
        elif self.min < 30:
            self.qhour = 2
        elif self.min < 45:
            self.qhour = 3
        else:
            self.qhour = 4
        self.hour = t.tm_hour  # hour of the day [0 .. 23]
        self.sec = t.tm_sec  # seconds of the min [0..59]
        self.wday = d.isocalendar()[2]
        if self.wday == 1:
            self.wday_name = "Monday"
        elif self.wday == 2:
            self.wday_name = "Tuesday"
        elif self.wday == 3:
            self.wday_name = "Wednesday"
        elif self.wday == 4:
            self.wday_name = "Thursday"
        elif self.wday == 5:
            self.wday_name = "Friday"
        elif self.wday == 6:
            self.wday_name = "Saturday"
        elif self.wday == 7:
            self.wday_name = "Sunday"
        else:  # should never reach this point
            raise DTError
        self.mday = t.tm_mday  # day of the month [1 .. 31]
        self.yday = t.tm_yday  # day of the year [1 .. 365/366] depending on leap year
        self.KW = d.isocalendar()[
            1
        ]  # week of the year [1 .. 52/53] aka 'Kalender week'
        self.month = t.tm_mon  # month of the year [1 .. 12]
        if self.month == 1:
            self.month_name = "January"
        elif self.month == 2:
            self.month_name = "February"
        elif self.month == 3:
            self.month_name = "March"
        elif self.month == 4:
            self.month_name = "April"
        elif self.month == 5:
            self.month_name = "May"
        elif self.month == 6:
            self.month_name = "June"
        elif self.month == 7:
            self.month_name = "July"
        elif self.month == 8:
            self.month_name = "August"
        elif self.month == 9:
            self.month_name = "September"
        elif self.month == 10:
            self.month_name = "October"
        elif self.month == 11:
            self.month_name = "November"
        elif self.month == 12:
            self.month_name = "December"
        else:  # should never reach this point
            raise DTError
        if self.month in [1, 2, 3]:
            self.quarter = 1
        elif self.month in [4, 5, 6]:
            self.quarter = 2
        elif self.month in [7, 8, 9]:
            self.quarter = 3
        else:
            self.quarter = 4
        self.year = t.tm_year  # year
        self.datetime = datetime.datetime(
            self.year, self.month, self.mday, self.hour, self.min, self.sec
        )
        self.date = f"{self.mday:02}{self.month:02}{self.year:04}"
        self.time = f"{self.hour:02}:{self.min:02}:{self.sec:02}"
        self.utc_offset = int((-self.tz * 3600) + (self.dst * 3600))
        # self.QDateTime.setOffsetFromUtc(int(utc_offset))  # timezone + day light saving
        # self.QDateTime.setSecsSinceEpoch(self.epoch)
        # self.QDate = self.QDateTime.date()
        # self.QTime = self.QDateTime.time()

    def boh(self):
        """
        Returns the epoch (is thus gmt based) for the Begin Of the Hour from the underlaying epoch.
        The epoch of the object remains unchanged.
        """
        return int(
            (
                datetime.datetime(self.year, self.month, self.mday, self.hour)
                - datetime.datetime(1970, 1, 1)
            ).total_seconds()
        )

    def eoh(self):
        """
        Returns the epoch (is thus gmt based) for the End Of the Hour from the underlaying epoch.
        The underlaying epoch of the object remains unchanged.
        """
        return self.boh() + 3600 - 1

    def bod(self):
        """
        Returns the epoch (is thus gmt based) for the Begin Of the Day from the underlaying epoch.
        The epoch of the object remains unchanged.
        """
        return int(
            (
                datetime.datetime(self.year, self.month, self.mday)
                - datetime.datetime(1970, 1, 1)
            ).total_seconds()
        )

    def eod(self):
        """
        Returns the epoch (is thus gmt based) for the End Of the Day from the underlaying epoch.
        The underlaying epoch of the object remains unchanged.
        """
        return self.bod() + (24 * 60 * 60) - 1

    def bow(self):
        """
        Returns the epoch (is thus gmt based) for the Begin Of the Week from the underlaying epoch.
        The underlaying epoch of the object remains unchanged.
        """
        temp = iso_to_gregorian(self.year, self.KW, 1)
        return int(
            (
                datetime.datetime(temp.year, temp.month, temp.day)
                - datetime.datetime(1970, 1, 1)
            ).total_seconds()
        )

    def eow(self):
        """
        Returns the epoch (is thus gmt based) for the End Of the Week from the underlaying epoch.
        The underlaying epoch of the object remains unchanged.
        """
        return self.bow() + (7 * 24 * 60 * 60) - 1

    def bom(self):
        """
        Returns the epoch (is thus gmt based) of the Begin Of the Month from the undelaying epoch.
        The underlying epoch of the object remains unchanged.
        """
        return DT(f"01{self.month:02}{self.year:04}").epoch

    def eom(self):
        """
        Returns the epoch (is thus gmt based) of the End Of the Month from the undelaying epoch.
        The underlying epoch of the object remains unchanged.
        """
        if self.month == 12:
            return DT(f"0101{self.year+1:04}").epoch - 1
        else:
            return DT(f"01{self.month+1:02}{self.year:04}").epoch - 1

    def boy(self):
        """
        Returns the epoch (is thus gmt based) of the Begin Of the Year from the underlaying epoch.
        The underlying epoch of the object remains unchanged.
        """
        return DT(f"0101{self.year:04}").epoch

    def eoy(self):
        """
        Returns the epoch (is thus gmt based) of the End Of the Year from the undelaying epoch.
        The undelaying epoch of the object remains unchanged.
        """
        return DT(f"0101{self.year+1:04}").epoch - 1

    def local(self):
        """
        Returns the epoch (is thus gmt based) for the LOCAL time.
        The underlaying epoch remains unchanged.
        """
        return self.epoch - (self.tz * 3600) + (abs(self.dst) * 3600)

    def __sub__(self, other):
        if self.__class__.__name__ == other.__class__.__name__:
            return TD(self.epoch - other.epoch)

        return NotImplemented

    def __lt__(self, other):
        if self.__class__.__name__ != other.__class__.__name__:
            return False
        if self.epoch < other.epoch:
            return True
        else:
            return False

    def __le__(self, other):
        if self.__class__.__name__ != other.__class__.__name__:
            return False
        if self.epoch <= other.epoch:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.__class__.__name__ != other.__class__.__name__:
            return False
        if self.epoch == other.epoch:
            return True
        else:
            return False

    def __ne__(self, other):
        if self.__class__.__name__ != other.__class__.__name__:
            return False
        if self.epoch != other.epoch:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.__class__.__name__ != other.__class__.__name__:
            return False
        if self.epoch > other.epoch:
            return True
        else:
            return False

    def __ge__(self, other):
        if self.__class__.__name__ != other.__class__.__name__:
            return False
        if self.epoch >= other.epoch:
            return True
        else:
            return False

    def __str__(self):
        # Monday, January 6 2014 @ 13:22:11 (Q1 2014)
        return "%s, %s %s %s @ %02d:%02d:%02d (Q%s %s)" % (
            self.wday_name,
            self.month_name,
            self.mday,
            self.year,
            self.hour,
            self.min,
            self.sec,
            self.quarter,
            self.datecode,
        )


class ChronoMeter(object):
    def __init__(self):
        self.reset()

    def reset(self):
        self.lap = 1
        self.laps = 0
        self.scoreboard = []

    def start(self):
        self.TimeStart = time.time()

    def stop(self):
        self.TimeStop = time.time()
        self.scoreboard.append(self.TimeStop - self.TimeStart)
        self.laps = self.lap
        self.lap = +1
        self.TimeStart = self.TimeStop

    def laps(self):
        return len(self.scoreboard)

    def time(self):
        retval = 0
        for lap in self.scoreboard:
            retval += lap
        return retval

    def laptimes(self):
        return self.scoreboard

    def averagelaptime(self):
        if self.laps != 0:
            return self.time() / self.laps
        else:
            return 0

    def __str__(self):
        return "Timed %f sec for %d laps (%f sec per lap)" % (
            self.time(),
            self.laps(),
            self.averagelaptime(),
        )
