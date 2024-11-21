def counting_sort_real(array, decimal_places=2):
    if not array:
        return []
    factor = 10 ** decimal_places
    rescaled_array = [int(x * factor) for x in array]

    min_value = min(rescaled_array)
    max_value = max(rescaled_array)

    count = [0] * (max_value - min_value + 1)

    for num in rescaled_array:
        count[num - min_value] += 1

    sorted_array = []
    for i, c in enumerate(count):
        sorted_array.extend([i + min_value] * c)

    return [x / factor for x in sorted_array]


array = [4.2, 2.1, 2.3, 8.1, 3.2, 3.1, 1.1]
print("Sorted Array in Ascending Order: ")
print(counting_sort_real(array))
