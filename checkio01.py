#Q1: The Most Wanted Letter
#URL : https://py.checkio.org/mission/most-wanted-letter/

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

    #original_listの中の各要素の出現回数を算出
    for x in original_list:
        element_freq = { key : original_list.count(key) for key in original_list }

    #element_freqの中で、value = 1のkeyのみ抽出し、new_listに入れる
    new_list = []

    for key,value in element_freq.items():
        if value == 1:
            new_list.append(key)

    #original_listのelementが、new_listに入っていない場合は、result_listに入れる
    result_list = []

    for element in original_list:
        if element not in new_list:
            result_list.append(element)

    return result_list

original_list = [10, 9, 10, 10, 9, 8]
print(unique_elements(original_list))


#Q3 : House Password
#URL : https://py.checkio.org/mission/house-password/

def check_password(password):

    #passwordのtextを、listに変化
    pw_list = [ element for element in password ]

    #数字、大文字、小文字の出現したかどうかをチェック
    check_list = []

    for element in pw_list:
        if element.islower() == True :
            check_list.append("小文字")
        elif element.isupper() == True :
            check_list.append("大文字")
        elif element.isdigit() == True :
            check_list.append("数字")

    #数字、大文字、小文字の出現回数の計算
    check_freq = { key : check_list.count(key) for key in check_list }

    #いずれも出現した場合はTrue、その他の場合はFalseを返す
    true_dict = { "大文字" : 1, "小文字" : 1, "数字" : 1 }
    result_list = []

    for key,value in true_dict.items():
        if key not in check_freq or len(check_list) < 10:
            result_list.append(False)
        else:
            result_list.append(True)

    for element in result_list:
        if False not in result_list:
            return True
        else:
            return False


password = "QwErTy911poqqqq"
print(check_password(password))
