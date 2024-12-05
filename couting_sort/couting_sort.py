def countingSort(array):
    size = len(array)
    output = [0] * size
    count = [0] * 10
    for i in range(0, size):
        count[array[i]] += 1

    for i in range(10):
        count[i] += count[i - 1]

    i = size - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1

    for i in range(size):
        array[i] = output[i]


array = [4, 2, 2, 8, 3, 3, 1]
countingSort(array)
print("Sorted Array in Ascending Order: ")
print(array)
