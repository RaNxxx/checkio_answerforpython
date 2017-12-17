def find_message(text):

    new_text = [element for element in text if element.isupper() == True]

    result = ""
    for element in new_text:
        result += element

    return result
