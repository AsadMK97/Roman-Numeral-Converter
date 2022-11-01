def printArabic(user_input):
    def value(user_input):
        if user_input == "I":
            return 1
        if user_input == "V":
            return 5
        if user_input == "X":
            return 10
        if user_input == "L":
            return 50
        if user_input == "C":
            return 100
        if user_input == "D":
            return 500
        if user_input == "M":
            return 1000
        return -1

    def process():
        result = 0
        num = 0

        while num < len(user_input):

            symbol_answer = value(user_input[num])

            if num + 1 < len(user_input):

                s2 = value(user_input[num + 1])

                if symbol_answer >= s2:
                    result = result + symbol_answer
                    num = num + 1
                else:
                    result = result + s2 - symbol_answer
                    num = num + 2
            else:
                result = result + symbol_answer
                num = num + 1
        if result == -2:
            print("Invalid input")
        elif result == -1:
            print("Invalid input")
        else:
            print(result)
        # print (type(result))

    process()
