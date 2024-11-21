def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def bucket_sort(arr):
    # Create a list of buckets
    buckets = []
    for i in range(len(arr)):
        buckets.append([])

    # Insert elements into their respective buckets
    for i in range(len(arr)):
        num = int(arr[i] * len(arr))
        buckets[num].append(arr[i])

    # Sort each bucket
    for i in range(len(arr)):
        buckets[i] = insertionSort(buckets[i])

    # Concatenate all buckets
    k = 0
    for i in range(len(arr)):
        for j in range(len(buckets[i])):
            arr[k] = buckets[i][j]
            k += 1
    return arr
