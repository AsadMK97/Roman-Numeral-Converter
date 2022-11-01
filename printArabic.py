def printArabic(user_input: str) -> int:
    roman_table = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    num = 0
    last = "I"
    for numeral in user_input[::-1]:
        if roman_table[numeral] < roman_table[last]:
            num -= roman_table[numeral]
        else:
            num += roman_table[numeral]
        last = numeral
    print (num)
    return num


##################################################### UNIT TESTS ########################################################


def test_printArabic():
    input = "I"
    expected_output = 1
    output = printArabic(input)
    assert output == expected_output


def test_to_printArabic_1_rta():
    """simple printArabic (I) == 1"""
    assert printArabic("I") == 1


def test_to_printArabic_2008_rta():
    """multi printArabic (MMVIII) == 2008"""
    assert printArabic("MMVIII") == 2008


def test_to_printArabic_4_rta():
    """simple subtraction printArabic (IV) == 4"""
    assert printArabic("IV") == 4


def test_to_printArabic_90_rta():
    """subtraction printArabic (XC) == 90"""
    assert printArabic("XC") == 90


def test_to_printArabic_3999_rta():
    """big printArabic (MMMCMXCIX) == 3999"""
    assert printArabic("MMMCMXCIX") == 3999
