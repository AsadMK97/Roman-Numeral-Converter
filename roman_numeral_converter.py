from printRoman import printRoman
from printArabic import printArabic


def to_roman_numeral():
    if __name__ == "__main__":
        user_num = input("Enter a number: ")
        try:
            roman_input = int(user_num)
            print("Roman value is:", end=" ")
            printRoman(roman_input)
        except ValueError:
            print("Invalid input")

def to_arabic_number():
    if __name__ == "__main__":
        user_input = input("Enter a numeral: ")
        print("Arabic value is: ", end="")
        printArabic(user_input)

converter_option = input("Select which converter to use: ")

if converter_option == ("1"):
    to_roman_numeral()
elif converter_option == ("2"):
    to_arabic_number()
else:
    print("invalid input")
