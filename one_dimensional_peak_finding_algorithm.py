def straightforward(arr):
    output = []
    for i in arr:
        if i == 0:
            if arr[i + 1] <= arr[i]:
                output.append(arr[i])

        elif i == len(arr) - 1:
            if arr[-1] >= arr[-2]:
                output.append(arr[i])

        else:
            if arr[i - 1] <= arr[i] >= arr[i + 1]:
                output.append(arr[i])

    return output


def divide_conquer(arr):
    output = []

    mid = len(arr) / 2
    left = mid - 1
    right = mid + 1

    if mid > 0 and arr[mid] < arr[left]:
        return divide_conquer(arr[:mid])

    elif mid < len(arr)-1 and arr[mid] < arr[right]:
        return divide_conquer(arr[mid:])

    else:
        output.append(arr[mid])

    return output


arr = [6, 7, 4, 3, 2, 1, 4, 5]

print straightforward(arr)
print divide_conquer(arr)
