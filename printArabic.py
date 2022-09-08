def printArabic(user_input):
    def value(romanNum):
        if romanNum == "I":
            return 1
        if romanNum == "V":
            return 5
        if romanNum == "X":
            return 10
        if romanNum == "L":
            return 50
        if romanNum == "C":
            return 100
        if romanNum == "D":
            return 500
        if romanNum == "M":
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
        print(result)
        # print (type(result))

    process()
