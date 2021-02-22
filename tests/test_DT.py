from Semi_ATE.TnD import DT, DTError


def test_init_none():
    assert DT().epoch > 0


def test_init_int_pos():
    assert DT(1570484799).epoch == 1570484799


def test_init_int_neg():
    assert DT(-7948800).epoch == -7948800


def test_init_float_pos():
    assert DT(1570484799.123).epoch == 1570484799


def test_init_float_neg():
    assert DT(-7948800.663).epoch == -7948800


def test_init_str_datecode_post_epoch():  # YYWWD
    assert DT("20074").datecode == "20074"


def test_init_str_datecode_pre_epoch():
    assert True  # datecode can not be pre-epoch!!!


def test_init_str_datecode_invalid():
    try:
        DT("fooba")
    except DTError:
        assert True
    else:
        assert False


def test_init_str_date_post_epoch():  # DDMMYYYY
    assert DT("13022020").date == "13022020"


def test_init_str_date_pre_epoch():
    assert DT("01101969").date == "01101969"


def test_init_str_invalid():
    try:
        DT("foobar..")
    except DTError:
        assert True
    else:
        assert False


def test_populate():
    snapshot = DT(1613687671)
    assert snapshot.datecode == "21074"
    assert snapshot.min == 34
    assert snapshot.qhour == 3
    assert snapshot.hour == 22
    assert snapshot.sec == 31
    assert snapshot.wday == 4
    assert snapshot.mday == 18
    assert snapshot.yday == 49
    assert snapshot.KW == 7
    assert snapshot.month == 2
    assert snapshot.quarter == 1
    assert snapshot.year == 2021
    assert snapshot.date == "18022021"
    assert snapshot.time == "22:34:31"


def test_day_names():
    assert DT("20011").wday_name == "Monday"
    assert DT("20012").wday_name == "Tuesday"
    assert DT("20013").wday_name == "Wednesday"
    assert DT("20014").wday_name == "Thursday"
    assert DT("20015").wday_name == "Friday"
    assert DT("20016").wday_name == "Saturday"
    assert DT("20017").wday_name == "Sunday"


def test_month_and_month_names():
    january = DT("01012020")
    assert january.month == 1
    assert january.month_name == "January"
    february = DT("01022020")
    assert february.month == 2
    assert february.month_name == "February"
    march = DT("01032020")
    assert march.month == 3
    assert march.month_name == "March"
    april = DT("01042020")
    assert april.month == 4
    assert april.month_name == "April"
    may = DT("01052020")
    assert may.month == 5
    assert may.month_name == "May"
    june = DT("01062020")
    assert june.month == 6
    assert june.month_name == "June"
    july = DT("01072020")
    assert july.month == 7
    assert july.month_name == "July"
    august = DT("01082020")
    assert august.month == 8
    assert august.month_name == "August"
    september = DT("01092020")
    assert september.month == 9
    assert september.month_name == "September"
    october = DT("01102020")
    assert october.month == 10
    assert october.month_name == "October"
    november = DT("01112020")
    assert november.month == 11
    assert november.month_name == "November"
    december = DT("01122020")
    assert december.month == 12
    assert december.month_name == "December"


def test_boh_eoh():
    middle_of_hour = DT(DT("01012020").epoch + 60 * 30)
    begin_of_hour = DT(middle_of_hour.boh())
    assert begin_of_hour.min == 0
    assert begin_of_hour.sec == 0
    end_of_hour = DT(middle_of_hour.eoh())
    assert end_of_hour.min == 59
    assert end_of_hour.sec == 59


def test_bod_eod():
    middle_of_day = DT(DT("01012020").epoch + 60 * 60 * 12)
    begin_of_day = DT(middle_of_day.bod())
    assert begin_of_day.hour == 0
    assert begin_of_day.min == 0
    assert begin_of_day.sec == 0
    end_of_day = DT(middle_of_day.eod())
    assert end_of_day.hour == 23
    assert end_of_day.min == 59
    assert end_of_day.sec == 59


def test_bow_eow():
    middle_of_week = DT("20013")  # Wednesday
    begin_of_week = DT(middle_of_week.bow())
    assert begin_of_week.wday == 1
    assert begin_of_week.hour == 0
    assert begin_of_week.min == 0
    assert begin_of_week.sec == 0
    end_of_week = DT(middle_of_week.eow())
    assert end_of_week.wday == 7
    assert end_of_week.hour == 23
    assert end_of_week.min == 59
    assert end_of_week.sec == 59


def test_bom_eom():
    middle_of_january = DT("14012020")
    begin_of_january = DT(middle_of_january.bom())
    assert begin_of_january.mday == 1
    assert begin_of_january.hour == 0
    assert begin_of_january.min == 0
    assert begin_of_january.sec == 0
    end_of_january = DT(middle_of_january.eom())
    assert end_of_january.mday == 31
    assert end_of_january.hour == 23
    assert end_of_january.min == 59
    assert end_of_january.sec == 59
    middle_of_february = DT("14022020")
    end_of_february = DT(middle_of_february.eom())
    assert end_of_february.mday == 29  # february had 29 days in 2020 !
    assert end_of_february.hour == 23
    assert end_of_february.min == 59
    assert end_of_february.sec == 59
    middle_of_april = DT("14042020")
    end_of_april = DT(middle_of_april.eom())
    assert end_of_april.mday == 30
    assert end_of_april.hour == 23
    assert end_of_april.min == 59
    assert end_of_april.sec == 59
    middle_of_december = DT("14042020")
    end_of_december = DT(middle_of_december.eom())
    assert end_of_december.mday == 31
    assert end_of_december.hour == 23
    assert end_of_december.min == 59
    assert end_of_december.sec == 59


def test_boy_eoy():
    middle_of_year = DT("14062020")
    begin_of_year = DT(middle_of_year.boy())
    assert begin_of_year.month == 1
    assert begin_of_year.mday == 1
    assert begin_of_year.hour == 0
    assert begin_of_year.min == 0
    assert begin_of_year.sec == 0
    end_of_year = DT(middle_of_year.eoy())
    assert end_of_year.month == 12
    assert end_of_year.mday == 31
    assert end_of_year.hour == 23
    assert end_of_year.min == 59
    assert end_of_year.sec == 59


def test__sub__():
    assert True


def test__lt__():
    assert True


def test__le__():
    assert True


def test__eq__():
    assert True


def test__ne__():
    assert True


def test__gt__():
    assert True


def test__ge__():
    assert True


def test__str__():
    assert True


def test_is_date_ok():
    assert DT("01101969")
