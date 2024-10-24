def bubble_sort(array):
    was_swapped = False
    zamiany = 0
    for i in range(len(array)):
        for j in range(len(array) - i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                zamiany += 1
                was_swapped = True
        if not was_swapped:
            break
    print(zamiany)


array = [64, 32, 52, 16, 13]
bubble_sort(array=array)
print(array)
