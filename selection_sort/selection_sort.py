def selection_sort(array):
    zamiany = 0
    przejścia = 0
    for i in range(len(array)-1):
        min_index = i
        przejścia += 1
        for j in range(i+1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
        zamiany += 1

    print(przejścia)
    print(zamiany)


array = [64, 26, 13, 21, 12]
selection_sort(array=array)
print(array)
