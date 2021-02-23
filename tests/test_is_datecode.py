from Semi_ATE.TnD.TnD import is_datecode

assert is_datecode("00540") is False
assert is_datecode("00XX0") is False
assert is_datecode("00010") is False
assert is_datecode("00018") is False
assert is_datecode("0001X") is False
assert is_datecode(0) is False
