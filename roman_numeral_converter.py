from tester import printRoman


def to_roman_numeral():
    if __name__ == "__main__":
        user_num = int(input("Enter a number: "))
        print("Roman value is:", end = " ")
        printRoman(user_num)




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







converter_option = input("Select which converter to use: ")

if converter_option == ("1") :
    to_roman_numeral()
elif converter_option == ("2") :
    to_arabic_number()
else:
    print("invalid input")