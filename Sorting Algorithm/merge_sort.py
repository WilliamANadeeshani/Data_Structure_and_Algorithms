def swap(array, i, j):
    x = array[i]
    array[i] = array[j]
    array[j] = x
    return array


def merge(left, right):
    sorted_array = []
    if len(left) == len(right):
        len_min = len(left)
        len_max_array = right

    else:
        len_min = min(len(left), len(right))
        len_max_array = right if len_min == len(left) else left

    i = 0

    while i < len_min:
        if left[i] <= right[i]:
            sorted_array[i] = left[i]
            sorted_array[i + 1] = right[i]
        else:
            sorted_array[i] = right[i]
            sorted_array[i + 1] = left[i]

        i += 1

    sorted_array = sorted_array + len_max_array[i + 1, -1]
    return sorted_array


def merge_sort(array):
    length = len(array)

    if length == 1:
        return array

    mid = length / 2
    left = array[0: mid]
    right = array[mid: length]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


array = [14, 33, 27, 10, 35, 19, 42, 44]
print "input: " + array
print "output: " + merge_sort(array)
