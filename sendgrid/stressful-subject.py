def is_stressful(subj):

    REDWORD = ["help", "asap", "urgent"]

    subj_lower = subj.lower()
    subj_split = subj_lower.split(" ")
    check_result = []

    for subj_text in subj_split:
        print(subj_text)
        for redword in REDWORD:
            print(redword)
            result = []
            for alphabet in redword:
                print(alphabet)
                if alphabet in subj_text:
                    result.append(True)
            print(result)
            if len(result) == len(redword):
                check_result.append(True)

    if subj.isupper() == True:
        check_result.append(True)

    if subj[-3::] == "!!!":
        check_result.append(True)

    if True in check_result:
        return True
    else:
        return False
