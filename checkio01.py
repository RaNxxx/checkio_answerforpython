#Q1: https://py.checkio.org/mission/most-wanted-letter/

import re

def count_alphabet(text):

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

text = "abe"
print(count_alphabet(text))


#Q2 : Non-unique Elements
#URL : https://py.checkio.org/mission/non-unique-elements/

def unique_elements(original_list):

    #original_listからユニークの要素をnew_listに抽出
    new_list = []
    new_list.append(original_list[0])


    for element in original_list:
        if element in original_list:
            new_list.append(element)

    #

    return original_list[0]

original_list = [1, 2, 3, 1, 3]
print(unique_elements(original_list))


#Q3 : House Password
#URL : https://py.checkio.org/mission/house-password/

'''
def check_pw(text):
'''
