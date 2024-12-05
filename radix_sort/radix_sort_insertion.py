def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def bucketSort(arr, number_of_buckets):
    max_value = max(arr)
    min_value = min(arr)
    range_of_elements = (max_value - min_value) / number_of_buckets

    buckets = []
    for i in range(number_of_buckets):
        buckets.append([])

    for i in range(len(arr)):
        j = int((arr[i] - min_value) / range_of_elements)
        if j != number_of_buckets:
            buckets[j].append(arr[i])
        else:
            buckets[number_of_buckets - 1].append(arr[i])

    for i in range(number_of_buckets):
        insertionSort(buckets[i])

    k = 0
    for i in range(number_of_buckets):
        for j in range(len(buckets[i])):
            arr[k] = buckets[i][j]
            k += 1
