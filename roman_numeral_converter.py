<<<<<<< HEAD
from tester import printRoman
=======
from printRoman import printRoman
from printArabic import to_arabic_number
>>>>>>> origin/to_roman_numeral


def to_roman_numeral():
    if __name__ == "__main__":
        user_num = int(input("Enter a number: "))
        print("Roman value is:", end = " ")
        printRoman(user_num)
<<<<<<< HEAD




def to_arabic_number():
    roman_input = input ("Enter roman number to convert: ")

    if "I" in roman_input :
        roman_input = (int(1))
    elif "V" in roman_input :
        roman_input = (int(5)) 
    elif "X" in roman_input :
        roman_input =(int(10))
    else:
     print("Invalid input")

    print (roman_input)
=======
    else:
        print("Invalid input")
>>>>>>> origin/to_roman_numeral



converter_option = input("Select which converter to use: ")

<<<<<<< HEAD



converter_option = input("Select which converter to use: ")

=======
>>>>>>> origin/to_roman_numeral
if converter_option == ("1") :
    to_roman_numeral()
elif converter_option == ("2") :
    to_arabic_number()
else:
    print("invalid input")