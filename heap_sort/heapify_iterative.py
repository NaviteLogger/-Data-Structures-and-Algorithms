import time


def heapify_iterative(arr, n, i):
    largest = i
    while True:
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[largest] < arr[left]:
            largest = left
        if right < n and arr[largest] < arr[right]:
            largest = right
        if largest == i:
            break
        arr[i], arr[largest] = arr[largest], arr[i]
        i = largest


def heapSort(arr):
    n = len(arr)
    for i in range(n//2 - 1, -1, -1):
        heapify_iterative(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify_iterative(arr, i, 0)


arr = []
for i in range(-100, 100):
    arr.append(i)
n = len(arr)
start = time.time()
heapSort(arr)
end = time.time()
print("Sorted array is")
for i in range(n):
    print("%d" % arr[i], end=" ")
print("Sorting took: ", end - start)
