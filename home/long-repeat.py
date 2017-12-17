import re
from itertools import groupby

def long_repeat(line):

    if line == "":
        return 0

    #new_listに、個々のアルファベット及び連続に出現する回数を算出
    #ここの改善点：最初からsetではなく、dictで作るか、setからlistではなく、dictにする方法が取れないかは要検討
    new_set = ({"{}:{}".format(ch, len(list(gen))) for ch, gen in groupby(line)})
    new_list = list(new_set)

    #最も多い回数を出す
    max_value_list = []

    for element in new_list:
        max_value_list.append(element.split(":")[1])

    max_value = max(max_value_list)
    int_value = int(max_value)

    return int_value
