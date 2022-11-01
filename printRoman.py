from unittest import result


def printRoman(user_num):
    roman = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I",
    }
    num_to_roman = ""
    for i in roman.keys():
        num_to_roman += roman[i] * (user_num // i)
        user_num %= i
    print (num_to_roman)
    return num_to_roman


############################################ UNIT TESTS ###########################################


# def test_printRoman():
#     input = 1
#     expected_output = "I"
#     output = printRoman(input)
#     assert output == expected_output


def test_printRoman_1_atn():
    # """simple printRoman (1) == I"""
    assert printRoman(1) == "I"


def test_printRoman_2008_atn():
    """multi printRoman (2008) == MMVIII"""
    assert printRoman(2008) == "MMVIII"


def test_printRoman_4_atn():
    """simple subtraction printRoman (4) == IV"""
    assert printRoman(4) == "IV"


def test_printRoman_90_atn():
    """subtraction printRoman (90) == XC"""
    assert printRoman(90) == "XC"


def test_printRoman_3999_atn():
    """big printRoman (3999) == MMMCMXCIX"""
    assert printRoman(3999) == "MMMCMXCIX"






##TESTING