def checkio(data):

    M = 1000
    D = 500
    C = 100
    L = 50
    X = 10
    V = 5
    I = 1

    result = ""

    if data/M >= 1:
        result += "M"*int(data/M)
        data = data - M*int(data/M)
    if data/D >= 1 and int(data/C) != 9:
        result += "D"*int(data/D)
        data = data - D*int(data/D)
    if int(data/C) == 9:
        result += "CM"
        data = data - 900
    if data/C >= 1 and int(data/C) != 4:
        result += "C"*int(data/C)
        data = data - C*int(data/C)
    if int(data/C) == 4:
        result += "CD"
        data = data - 400
    if data/L >= 1 and int(data/X) != 9:
        result += "L"*int(data/L)
        data = data - L*int(data/L)
    if int(data/X) == 9:
        result += "XC"
        data = data - 90
    if data/X >= 1 and int(data/X) != 4:
        result += "X"*int(data/X)
        data = data - X*int(data/X)
    if int(data/X) == 4:
        result += "XL"
        data = data - 40
    if data/V >= 1 and int(data/I) != 9:
        result += "V"*int(data/V)
        data = data - V*int(data/V)
    if int(data/I) == 9:
        result += "IX"
        data = data - 9
    if data/I >= 1 and int(data/I) != 4:
        result += "I"*int(data/I)
        data = data - I*int(data/I)
    if int(data/I) == 4:
        result += "IV"

    return result
