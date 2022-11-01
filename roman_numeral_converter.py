# import click
from printRoman import printRoman
from printArabic import printArabic


def to_roman_numeral(user_num):
    try:
        roman_output = int(user_num)
        print("Roman value is:", end=" ")
        printRoman(roman_output)
    except ValueError:
        print("Invalid input")


def to_arabic_number(user_input):
    print("Arabic value is: ", end="")
    printArabic(user_input)


if __name__ == "__main__":

    def converter_prompt(converter_option=None):
        if converter_option is None:
            converter_option = input("Select which converter to use: ")

        if converter_option == ("1"):
            user_num = input("Enter a number: ")
            to_roman_numeral(user_num)
        elif converter_option == ("2"):
            user_input = input("Enter a numeral: ")
            to_arabic_number(user_input)
        else:
            print("Invalid input")

    converter_prompt()


# @click.command()
# @click.option(
#     "--converter",
#     prompt="Enter a converter to use: ",
#     help="""1 is roman to arabic.
#     2 is arabic to roman.""",
# )
# @click.option('--roman', prompt='Enter a numeral', help='Enter a Roman numeral to convert into arabic')
# @click.option('--arabic', prompt='Enter a number', help='Enter an Arabic number to conver into roman')
# def hello(converter):
#     if converter == "1":
#         user_num = input("Enter a number: ")
#         to_roman_numeral(user_num)
#     elif converter == "2":
#         user_input = input("Enter a numeral: ")
#         to_arabic_number(user_input)
#     else:
#         print("Invalid")

##################################################### TESTING CODE ######################################################


def test_to_roman_numeral_1_rta():
    # Given
    input = 1
    excepted_output = "I"
    # When
    output = to_roman_numeral(input)
    # Then
    assert output == excepted_output


# def test_to_arabic_number_2009_rta():
#     # Given
#     input = "MMVIII"
#     expected_output = 2008
#     # When
#     output = to_arabic_number(input)
#     # Then
#     assert output == expected_output
