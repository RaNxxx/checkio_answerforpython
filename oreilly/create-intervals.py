def create_intervals(data):

    data_list = list(data)
    sorted_data = sorted(data_list)
    print(sorted_data)

    #直前の要素と差が1以上のものを取る
    start = []

    for number in sorted_data:
        if sorted_data.index(number) == 0:
            start.append(number)
        else:
            if number != sorted_data[sorted_data.index(number)-1] + 1:
                start.append(number)

    print(start)

    #直後のものと差が1以上のものを取る
    end = []

    for number in sorted_data:
        if sorted_data.index(number) != len(sorted_data) -1 and sorted_data.index(number) != 0:
            if number != sorted_data[sorted_data.index(number)+1] - 1:
                end.append(number)
        elif sorted_data.index(number) == len(sorted_data) -1:
            end.append(number)

    print(end)

    #startとendのセットを作る
    return_list = []

    for number in start:
        if len(start) > len(end):
            if start.index(number) == 0:
                return_list.append((number,number))
            else:
                return_list.append((number,end[start.index(number)-1]))
        if len(start) == len(end):
            return_list.append((number,end[start.index(number)]))

    return return_list
