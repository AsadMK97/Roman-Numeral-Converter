# import roman_numeral_converter
from printRoman import printRoman
from printArabic import printArabic


def test_to_arabic_number_1_rta():
    assert printArabic("I") == 1


# # def test_to_arabic_number_2008_rta():
# #     assert to_arabic_number("MMVIII") == 2008


def test_to_arabic_number_1():
    # Given
    input = "I"
    excepted_output = 1
    # When
    output = printRoman(input)
    # Then
    assert output == excepted_output
