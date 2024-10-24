import random


def selection_sort(arr):
    zamiany = 0
    przejścia = 0
    for i in range(len(arr)-1):
        min_index = i
        przejścia += 1
        for j in range(i+1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        zamiany += 1

    print("Licznik zamian dla selection:")
    print(przejścia)
    print("Licznik przejść dla selection:")
    print(zamiany)


# def shell(arr):
#     liczba_zamian_dla_shella = 0
#     przejscia = 0
#     gap = 1
#     while gap < len(arr):
#         j = gap
#         przejscia += 1
#         while j < len(arr):
#             i = j-gap

#             while i >= 0:
#                 if arr[i+gap] >= arr[i]:
#                     break
#                 else:
#                     liczba_zamian_dla_shella += 1
#                     arr[i+gap], arr[i] = arr[i], arr[i+gap]
#                 i = i-gap
#             j += 1
#         gap = gap * 2

#     print("Licznik zamian dla shell:")
#     print(liczba_zamian_dla_shella)
#     print("Licznik przejść dla shell:")
#     print(przejscia)


def shell(arr):
    n = len(arr)
    h = 1
    liczba_zamian_dla_shella = 0
    przejscia = 0
    while h < n/3:
        h = 3*h + 1

    while h >= 1:
        for i in range(h, n):
            for j in range(i, h-1, -h):
                przejscia += 1
                if arr[j] < arr[j - h]:
                    swap = arr[j-h]
                    arr[j-h] = arr[j]
                    arr[j] = swap
        h = h//3

    print("Licznik zamian dla shell:")
    print(liczba_zamian_dla_shella)
    print("Licznik przejść dla shell:")
    print(przejscia)


def insertion_sort(arr):
    liczba_zamian_dla_insertion = 0
    liczba_przejsc = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        liczba_przejsc += 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            liczba_zamian_dla_insertion += 1
            j -= 1
        arr[j+1] = key

    print("Licznika zamian dla insertion:")
    print(liczba_zamian_dla_insertion)
    print("Licznik przejść dla insertion:")
    print(liczba_przejsc)


def bubble_sort(arr):
    was_swapped = False
    zamiany = 0
    przejscia = 0
    for i in range(len(arr)):
        przejscia += 1
        for j in range(len(arr) - i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                zamiany += 1
                was_swapped = True
        if not was_swapped:
            break

    print("Licznik zamian dla bubble:")
    print(zamiany)
    print("Licznik przejść dla bubble:")
    print(przejscia)


array = []
for i in range(20):
    array.append(random.randint(0, 100))

selection_sort(array)
print("\n")

array = []
for i in range(20):
    array.append(random.randint(0, 100))

shell(array)
print("\n")

array = []
for i in range(20):
    array.append(random.randint(0, 100))

insertion_sort(array)
print("\n")

array = []
for i in range(20):
    array.append(random.randint(0, 100))

bubble_sort(array)
print("\n")
