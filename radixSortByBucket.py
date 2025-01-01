def insertionSort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def bucketSort(arr, numberOfBuckets):
    _arr = []
    max_el = max(arr)
    min_el = min(arr)
    number_range = (max_el - min_el) / numberOfBuckets
    for i in range(numberOfBuckets):
        _arr.append([])
    for i in arr:
        bucket_index = int((i - min_el) / number_range)
        if bucket_index == numberOfBuckets:
            bucket_index = numberOfBuckets - 1
        _arr[bucket_index].append(i)

    for i in range(numberOfBuckets):
        insertionSort(_arr[i])

    k = 0
    for i in range(numberOfBuckets):
        for j in range(len(_arr[i])):
            arr[k] = _arr[i][j]
            k += 1
    return arr


def radixSort(arr):
    max1 = max(arr)
    exp = 1
    while max1 / exp >= 1:
        bucketSort(arr, exp)
        exp *= 10


arr = [170, 45, 75, 90, 802, 24, 2, 66]
radixSort(arr)
print(arr)