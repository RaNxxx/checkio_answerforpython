def checkio(data):

    not_unique_list = []

    for element in data:
        if data.count(element) > 1:
            not_unique_list.append(element)

    return not_unique_list
