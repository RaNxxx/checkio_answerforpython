def second_index(text, symbol):

    #symbolがtextに出現するindexをlistに
    index_list = [ i for i, v in enumerate(text) if v == symbol ]

    if len(index_list) >= 2:
        return index_list[1]
    else:
        return None
