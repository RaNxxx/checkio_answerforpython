def verify_anagrams(first_word, second_word):

    first_list = [element.lower() for element in first_word if element != " "]
    second_list = [element.lower() for element in second_word if element != " "]

    check_list = []

    for element in second_list:
        if element in first_list and second_list.count(element) == first_list.count(element):
            check_list.append(True)
        else:
            check_list.append(False)

    for element in first_list:
        if element not in second_list:
            check_list.append(False)

    if False in check_list:
        return False
    else:
        return True
