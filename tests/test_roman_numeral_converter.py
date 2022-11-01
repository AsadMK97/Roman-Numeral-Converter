# import pytest

# import os
# print(os.getcwd())

import roman_numeral_converter

# def test_to_arabic_number_1_rta():
#     assert to_arabic_number("I") == 1

# # def test_to_arabic_number_2008_rta():
# #     assert to_arabic_number("MMVIII") == 2008


def test_to_arabic_number_1():
    # Given
    input = "I"
    excepted_output = 1
    # When
    output = roman_numeral_converter.to_arabic_number(input)
    # Then
    assert output == excepted_output
