import math
import beams

def test_str_to_int():
    string_1 = "43"
    string_2 = "-2000"

    assert beams.str_to_int(string_1) == 43
    assert beams.str_to_int(string_2) == -2000

def test_str_to_float():
    string_1 = "43"
    string_2 = "-2000"
    string_3 = "324.625"

    assert beams.str_to_float(string_1) == 43.0
    assert beams.str_to_float(string_2) == -2000.0
    assert beams.str_to_float(string_3) == 324.625