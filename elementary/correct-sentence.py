def correct_sentence(text):

    new_text = text[0].upper() + text[1:]

    if "." not in new_text:
        new_text = new_text + "."
    else:
        new_text

    return new_text
