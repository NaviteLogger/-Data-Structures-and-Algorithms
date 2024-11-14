def partition(arr, low, high):

    pivot = arr[low]
    i = low - 1
    j = high + 1

    while True:
        i += 1
        while arr[i] < pivot:
            i += 1

        j -= 1
        while arr[j] > pivot:
            j -= 1

        if i >= j:
            return j

        arr[i], arr[j] = arr[j], arr[i]


def quicksort(arr, low, high):
    if low >= 0 and high >= 0 and low < high:
        p = partition(arr, low, high)
        quicksort(arr, low, p)
        quicksort(arr, p+1, high)


array = [10, 4, 7, 6, 3, 2, 9, 8]
quicksort(array, 0, len(array)-1)
print(array)
