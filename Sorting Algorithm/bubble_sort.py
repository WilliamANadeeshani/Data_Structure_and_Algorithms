def swap(array, i, j):
    x = array[i]
    array[i] = array[j]
    array[j] = x
    return array


def bubbleSort(array):
    print "input: " + str(array)
    array_length = len(array)

    for y in range(0, array_length - 1):
        for x in range(0, array_length - 1):
            if array[x] > array[x + 1]:
                array = swap(array, x, x+1)

    print "output: " + str(array)


bubbleSort([14, 33, 27, 35, 10])
