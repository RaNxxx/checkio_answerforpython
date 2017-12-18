def checkio(first, second):

    first_list = first.split(",")
    second_list = second.split(",")

    check_list = []

    for word in first_list:
        if word in second_list:
            check_list.append(word)

    for word in second_list:
        if word in first_list and word not in check_list:
            check_list.append(word)

    sorted_list = sorted(check_list)

    check_text = ",".join(sorted_list)

    return check_text
