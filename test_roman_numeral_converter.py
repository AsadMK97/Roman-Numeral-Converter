# import pytest

from roman_numeral_converter import to_arabic_number
from roman_numeral_converter import to_roman_numeral


def test_to_arabic_number_1_rta():
    assert to_arabic_number("I") == 1

def test_to_arabic_number_2008_rta():
    assert to_arabic_number("MMVIII") == 2008





def test_to_roman_numeral_1():
    assert to_roman_numeral(1) == "I"