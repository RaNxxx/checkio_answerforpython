def checkio(number):

    number_str = str(number)
    number_list = [int(element) for element in number_str if element != "0"]

    result = 1
    for element in number_list:
        print(element)
        result = result * element

    return result
