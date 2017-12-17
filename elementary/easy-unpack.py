def easy_unpack(elements):

    pack_list = []

    pack_list.append(elements[0])
    pack_list.append(elements[2])
    pack_list.append(elements[-2])

    pack_tuple = tuple(pack_list)

    return pack_tuple
