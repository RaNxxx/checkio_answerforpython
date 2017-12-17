def checkio(words):

    def check_if_string(target_list):

        for e in target_list:
            try:
                int_value = int(e)
                return False
            except ValueError:
                pass

        return True

    word_list = words.split(" ")

    group_by = 3
    new_list = [word_list[i:i + group_by] for i in range(0, len(word_list)) if len(word_list[i:i + group_by]) >= 3]

    check_list = []
    element_result = 0

    for l in new_list:
        print(l)
        a = check_if_string(l)
        check_list.append(a)

    if True not in check_list:
        return False
    else:
        return True
