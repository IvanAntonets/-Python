import pytest
from string_utils import StringUtils

string_utils = StringUtils()

"""capitilize"""
def test_capitilize():
    # Positive
    assert string_utils.capitilize("skypro") == "Skypro"
    assert string_utils.capitilize("hay jack") == "Hay jack"
    assert string_utils.capitilize("123") == "123"
    assert string_utils.capitilize("овощи123") == "Овощи123"
    # Negative
    assert string_utils.capitilize("") == ""
    assert string_utils.capitilize(" ") == " "
    assert string_utils.capitilize("hello Bob") == "Hello Bob"
    assert string_utils.capitilize("@") == "@"

"""trim"""
def tesr_trim():
    # Positive
    assert string_utils.trim(" skypro") == "Skypro"
    assert string_utils.trim(" Hay jack") == "Hay jack"
    assert string_utils.trim(" 123") == "123"
    # Negative
    assert string_utils.trim("") == ""
    assert string_utils.trim("123") == "123"
    assert string_utils.trim(" ") == " "

@pytest.mark.xfail()
def test_trim_with_numbers_input():
    assert string_utils.trim("123") == "123"

"""to_list"""
@pytest.mark.parametrize('string, delimeter, result',[
    # Positive
    ("h,e,l,l,o", ",", ["h", "e", "l", "l", "o"]),
    ("п,р,и,в,е,т", ",", ["п", "р", "и", "в", "е", "т"]),
    ("1,2,3,4,5", ",", ["1", "2", "3", "4", "5"]),
    ("!,@,#,$", ",", ["!", "@", "#", "$"]),
    # Negative
    ("", None, []),
    ("video", None, ["v", "i", "d e", "o"]) 
]) 
def test_to_list(string, delimeter, result):
    if delimeter is None:
        res = string_utils.to_list(string)
    else:
        res = string_utils.to_list(string, delimeter)
    assert res == result

"""contains"""
@pytest.mark.parametrize('string, symbol, result',[
    ("FlyEmirates", "F", True),
    ("Oleg", "l", True),
    ("123", "3", True),
    ("Машина", "М", True),
    ("SkyPro", "K", False),
    ("4455", "6", False),
    ("Auto", "a", False),
    ("tetrad", "", False)
])
def test_contains(string, symbol, result):
    res = string_utils.contains(string, symbol)
    assert res == result 

"""delete_symbol"""
@pytest.mark.parametrize('string, symbol, result',[
    # Positive
    ("Fly Emirates", " ", "FlyEmirates"),
    ("Oleg", "l", "Oeg"),
    ("123", "3", "12"),
    ("Машина", "М", "ашина"),
    # Negative
    ("", "", ""),
    ("Овощи", "з", "Овощи"),
    ("", "a", ""),
    ("tetrad", " ", "tetrad")
])
def test_delete_symbol(string, symbol, result):
    res = string_utils.delete_symbol(string, symbol)
    assert res == result 

"""starts_with"""
@pytest.mark.parametrize('string, symbol, result',[
    ("Auto", "A", True),
    ("Igor", "I", True),
    ("54321", "5", True),
    ("Машина", "М", True),
    ("", "", True),
    ("Milan", "m", False),
    ("45678", "7", False),
    ("Skoda", "K", False),
    ("", "t", False),
    ("world", "W", False)
])
def test_starts_with(string, symbol, result):
    res = string_utils.starts_with(string, symbol)
    assert res == result 

"""end_with"""
@pytest.mark.parametrize('string, symbol, result',[
    ("Auto", "o", True),
    ("IgoR", "R", True),
    ("54321", "1", True),
    ("Машина", "а", True),
    ("", "", True),
    ("Milan", "N", False),
    ("45678", "4", False),
    ("Skoda", "D", False),
    ("", "t", False),
    ("worlD", "d", False)
])
def test_end_with(string, symbol, result):
    res = string_utils.end_with(string, symbol)
    assert res == result 

"""is_empty"""
@pytest.mark.parametrize('string, result',[
    ("", True),
    (" ", True),
    ("   ", True),
    ("Slovo", False),
    ("privet medved", False),
    ("45678", False),
    (" t ", False),
])
def test_is_empty(string, result):
    res = string_utils.is_empty(string)
    assert res == result 

"""list_to_string"""
@pytest.mark.parametrize('lst, joiner, result',[
    # Positive
    (["h", "e", "l", "l", "o"], ",", "h,e,l,l,o"),
    (["п", "р", "и", "в", "е", "т"], "", "привет"),
    (["1", "2", "3", "4", "5"], "-", "1-2-3-4-5"),
    (["!, @, #, $"], None, "!, @, #, $"),
    (["One", "Two"], "Polovina", "OnePolovinaTwo"),
    # # Negative
    ([], None, ""),
    ([], "video", ""),
    ([], "-", "") 
]) 
def test_list_to_string(lst, joiner, result):
    if joiner == None:
        res = string_utils.list_to_string(lst)
    else:
        res = string_utils.list_to_string(lst, joiner)
    assert res == result