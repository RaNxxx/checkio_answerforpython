import re

def checkio(text):

    #大文字と小文字を区別しない
    new_text = text.lower()

    alphabet_dict = { x for x in new_text }
    alphabet_freq = {}

    #アルファベット出現の頻度を計算
    for x in alphabet_dict:
        alphabet_freq = { x : new_text.count(x) for x in alphabet_dict if re.match('[a-z]', x) != None }

    freq_count = sorted(alphabet_freq.items(), key=lambda x: x[1],reverse=True)

    #valueが最も大きいキーが複数存在する場合、アルファベット順で最初のものを出す

    max_value = freq_count[0][1]

    final_list = []

    for element in freq_count:
        if element[1] == max_value:
            final_list.append(element[0])

    final_alphabet = sorted(final_list)


    return final_alphabet[0]
