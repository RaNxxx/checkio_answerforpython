def count_words(text, words):

    #word_listから要素がユニークに含まれるlistを作成
    unique_list = []

    for element in words:
        if element not in unique_list:
            unique_list.append(element)

    #wordを全て小文字のintに変換する
    small_word = text.lower()

    #それぞれの要素がwordに含まれているかどうかをチェック
    count_result = 0

    for element in unique_list:
        if element in small_word:
            count_result = count_result + 1

    return count_result
