from Semi_ATE.TnD.TnD import is_date

assert is_date("32000000") is False
assert is_date("00130000") is False
assert is_date(0) is False