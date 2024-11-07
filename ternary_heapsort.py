def heapify(arr, n, i):
    largest = i
    left = 3 * i + 1
    middle = 3 * i + 2
    right = 3 * i + 3

    if left < n and arr[largest] < arr[left]:
        largest = left

    if middle < n and arr[largest] < arr[middle]:
        largest = middle

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heapSort(arr):
    n = len(arr)

    for i in range(n//3 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


arr = [4, 10, 3, 5, 1]
n = len(arr)
heapSort(arr)
print("Sorted array is")
for i in range(n):
    print("%d" % arr[i], end=" ")
