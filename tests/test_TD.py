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

