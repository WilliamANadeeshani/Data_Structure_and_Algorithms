def swap(array, i, j):
    x = array[i]
    array[i] = array[j]
    array[j] = x
    return array


def get_min(array):
    min = array[0]
    index = 0

    for x in range(1, len(array)):
        if array[x] < min:
            min = array[x]
            index = x

    return index


def selection_sort(array):
    print "input: " + array
    length = len(array)

    for x in range(0, length):
        min_value_index = get_min(array)
        swap(array, array[x], array[min_value_index])

    print "input: " + array

