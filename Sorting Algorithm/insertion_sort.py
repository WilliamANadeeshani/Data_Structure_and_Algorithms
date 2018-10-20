def swap(array, i, j):
    x = array[i]
    array[i] = array[j]
    array[j] = x
    return array


def insertion_sort(array):
    print "input: " + str(array)
    array_length = len(array)

    for x in range(0, array_length - 1):
        if array[x] > array[x + 1]:
            for y in range(x + 1, 0, -1):
                if array[y] < array[y - 1]:
                    swap(array, y - 1, y)
                else:
                    break

    print "output: " + str(array)


insertion_sort([14, 33, 27, 10, 35, 19, 42, 44])
