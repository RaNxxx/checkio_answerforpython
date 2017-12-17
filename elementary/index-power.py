def index_power(array, n):

    if len(array) > n:
        result = array[n]**n
    else:
        result = -1

    return result
