from printRoman import printRoman
from printArabic import printArabic


def to_roman_numeral():
    if __name__ == "__main__":
        user_num = int(input("Enter a number: "))
        print("Roman value is:", end=" ")
        printRoman(user_num)
    else:
        print("Invalid input")


def to_arabic_number():
    if __name__ == "__main__":
        user_input = input("Enter a numeral: ")
        print("Arabic value is: ", end="")
        printArabic(user_input)
    else:
        print("Invalid input")


converter_option = input("Select which converter to use: ")

if converter_option == ("1"):
    to_roman_numeral()
elif converter_option == ("2"):
    to_arabic_number()
else:
    print("invalid input")
