def first_word(text):

    text = text.replace(","," ")
    text = text.replace("."," ")
    sep_text = text.split(" ")

    for element in sep_text:
        if element != "":
            return element
