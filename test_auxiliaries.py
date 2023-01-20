from auxiliaries import *

def test_increase_0():
    assert increase("1234", 2, 8) == "3456"

def test_increase_1():
    assert increase("0502", 2, 9) == "2734"

def test_increase_2():
    assert increase("7030", 3, 9) == "0364"

def test_compare_0():
    assert compare("17575", "95304") == (0, 1)

def test_compare_1():
    assert compare("262137", "213769") == (1, 4)

def test_compare_2():
    assert compare("27052030", "19407732") == (1, 3)