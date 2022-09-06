
def printArabic(user_num):
    num = [1, 4, 5, 9, 10, 40, 50, 90,
        100, 400, 500, 900, 1000]
    symbol = ["I", "IV", "V", "IX", "X", "XL","L",
                "XC", "C", "CD", "D", "CM", "M"]
    i = 12
    
    while user_num:
        div = user_num // num[i]
        user_num %= num[i]

        while div:
            print(symbol[i], end = "")
            div -= 1
        i -= 1
