def checkio(expression):

    BRACKETS = ["(", ")", "[", "]", "{","}"]
    brackets_list = [ element for element in expression if element in BRACKETS]

    temp_list = []

    left_side = ["(", "[", "{"]
    right_side = [")", "]", "}"]

    for element in brackets_list:
        if element in left_side:
            temp_list.append(element)
        elif element in right_side:
            if left_side[right_side.index(element)] in temp_list:
                temp_list.pop()
            else:
                temp_list.append(element)

    if temp_list == []:
        return True
    else:
        return False
