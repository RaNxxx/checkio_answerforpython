def checkio(data):

    data.sort()
    print(data)
    len_of_data = len(data)
    median_data = []

    if len_of_data %2 == 0:
        median_data.append(data[int(len_of_data/2-1)])
        median_data.append(data[int(len_of_data/2)])
    if len_of_data %2 != 0:
        median_data.append(data[int(len_of_data/2)])

    median = sum(median_data)/len(median_data)

    return median
