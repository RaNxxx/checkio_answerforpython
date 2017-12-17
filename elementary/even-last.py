def checkio(array):

    if array == []:
        end = 0
    else:
        end = array[-1]
    totalsum = sum(array[0::2])
    result = end*totalsum

    return result
