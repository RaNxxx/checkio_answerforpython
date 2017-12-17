def checkio(data):

    #passwordのtextを、listに変化
    pw_list = [ element for element in data ]

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
