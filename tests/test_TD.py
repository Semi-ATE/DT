import time

from Semi_ATE.TnD.TnD import DT, TD


try:
    _ = DT()
    _ = _ - DT(_.epoch + 1)
except:
    assert False
else:
    assert True

one = 34858861
two = 2 * one

assert TD(one).__str__() == "1 year 1 month 1 week 1 day 1 hour 1 minute 1 second"
assert TD(two).__str__() == "2 years 2 months 2 weeks 2 days 2 hours 2 minutes 2 seconds"

assert TD(one).seconds() == one
assert TD(one).minutes() == 580981.0166666667
assert TD(one).hours() == 9683.016944444444
assert TD(one).days() == 403.45903935185186
assert TD(one).weeks() == 57.63700562169312
assert TD(one).months() == 13.264406773211567
assert TD(one).years() == 1.105367231100964
