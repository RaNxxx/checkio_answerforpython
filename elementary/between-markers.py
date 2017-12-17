import re
def between_markers(text: str, begin: str, end: str) -> str:
    if begin not in text and end not in text: return text
    if begin not in text: text = begin + text
    if end not in text: text = text + end
    if text.index(begin) > text.index(end): return ""

    pattern = re.escape(begin) + "(.*)" + re.escape(end)
    match_object = re.search(pattern, text)

    return match_object.group(1)
