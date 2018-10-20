def quickSort(alist):
    quickSortHelper(alist, 0, len(alist) - 1)


def quickSortHelper(alist, first, last):
    if first < last:
        splitpoint = partition(alist, first, last)

        quickSortHelper(alist, first, splitpoint - 1)
        quickSortHelper(alist, splitpoint + 1, last)


def partition(array, first, last):
    pivot = array[first]

    low = first + 1
    high = last

    done = False
    while not done:

        while low <= high and array[low] <= pivot:
            low = low + 1

        while array[high] >= pivot and high >= low:
            high = high - 1

        if high < low:
            done = True
        else:
            temp = array[low]
            array[low] = array[high]
            array[high] = temp

    temp = array[first]
    array[first] = array[high]
    array[high] = temp

    return high


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quickSort(alist)
print(alist)
