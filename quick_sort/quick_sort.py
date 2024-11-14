import random
# low to index pierwszego elementu tablicy
# high to index ostatniego elementu tablicy


def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1


def insertionSort(arr, low, high):
    for i in range(low + 1, high + 1):
        key = arr[i]
        j = i - 1
        while j >= low and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# def quickSort(arr, low, high):
#     if len(arr) == 1:
#         return arr
#     if low < high:
#         pi = partition(arr, low, high)
#         quickSort(arr, low, pi-1)
#         quickSort(arr, pi+1, high)


def quickSortAlternative(arr, low, high):
    if len(arr) == 0:
        return arr
    if low < high:
        pi = partition(arr, low, high)
        if (len(arr)-pi) > len(arr)//2:
            quickSortAlternative(arr, low, pi-1)
            quickSortAlternative(arr, pi+1, high)
        else:
            quickSortAlternative(arr, pi+1, high)
            quickSortAlternative(arr, low, pi-1)


def quickSortFast(arr, low, high):
    if high - low < 10:
        insertionSort(arr, low, high)
    if low < high:
        pi = partition(arr, low, high)
        if (len(arr)-pi) > len(arr)//2:
            quickSortAlternative(arr, low, pi-1)
            quickSortAlternative(arr, pi+1, high)
        else:
            quickSortAlternative(arr, pi+1, high)
            quickSortAlternative(arr, low, pi-1)


arr = []
for i in range(1, 10000):
    arr.append(random.randint(1, 100000))
print(arr)
print("\n")
quickSortFast(arr, 0, len(arr)-1)
print(arr)
