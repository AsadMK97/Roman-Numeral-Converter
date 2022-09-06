def to_arabic_number():
    def value(romanNum):
        if (romanNum == 'I'):
            return 1
        if (romanNum == 'V'):
            return 5
        if (romanNum == 'X'):
            return 10
        if (romanNum == 'L'):
            return 50
        if (romanNum == 'C'):
            return 100
        if (romanNum == 'D'):
            return 500
        if (romanNum == 'M'):
            return 1000
        return -1


    def process():
        res = 0
        i = 0

        while (i < len(user_input)):

            # Getting value of symbol s[i]
            s1 = value(user_input[i])

            if (i + 1 < len(user_input)):

                # Getting value of symbol s[i + 1]
                s2 = value(user_input[i + 1])

                # Comparing both values
                if (s1 >= s2):

                    # Value of current symbol is greater
                    # or equal to the next symbol
                    res = res + s1
                    i = i + 1
                else:

                    # Value of current symbol is greater
                    # or equal to the next symbol
                    res = res + s2 - s1
                    i = i + 2
            else:
                res = res + s1
                i = i + 1

        print (res)



    user_input = input("Enter a numeral: ")
    process()