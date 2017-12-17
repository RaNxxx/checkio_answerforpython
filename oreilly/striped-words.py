import re
VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"

def checkio(text):

    text = text.replace("."," ")
    text = text.replace(","," ")
    word_list = [element.upper() for element in text.split(" ") if element != "" and re.search('[0-9]',element) == None]
    print(word_list)

    #各単語の各アルファベットに母音か子音かを判定
    text_result = []

    for word in word_list:
        word_result = []
        for alphabet in word:
            if alphabet in VOWELS:
                word_result.append("V")
            if alphabet in CONSONANTS:
                word_result.append("C")

        text_result.append(word_result)

    #各判定結果を、その直前の判定結果と見比べ、同じだったらFalseを返す
    storage_result = []

    for result_list in text_result:
        storage = []
        for result in result_list:
            if storage == []: storage.append(result)
            elif result != storage[-1]: storage.append(result)
            elif result == storage[-1]: storage.append(False)

        storage_result.append(storage)

    #Falseが含まれない、かつ、len>=2のものの個数をカウント
    count_list = []
    for final_result in storage_result:
        if False not in final_result and len(final_result) >= 2:
            count_list.append(True)

    if True in count_list:
        return count_list.count(True)
    else:
        return 0
