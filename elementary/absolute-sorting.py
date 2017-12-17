import math

def checkio(numbers_array):
    absolute_list = []

    for element in numbers_array:
        if element < 0:
            absolute_list.append(-element)
        else:
            absolute_list.append(element)

    sort_list = sorted(absolute_list)

    return_list = []

    for element in sort_list:
        for e in numbers_array:
            if math.fabs(e) == element:
                return_list.append(e)
            else:
                pass

    return return_list
