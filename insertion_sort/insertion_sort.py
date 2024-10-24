import random
import timeit

arr = [5,4,1,20,30,2,7,0]

# for i in range(10000):
#     array.append(random.randint(0,100000))

def insertion_sort(arr):
    liczba_zamian_dla_insertion = 0
    for i in range(1, len(array)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            liczba_zamian_dla_insertion += 1
            j -= 1
        arr[j+1] = key

    print(liczba_zamian_dla_insertion)

array = [5,4,1,20,30,2,7,0]

def shell(arr, n):
    liczba_zamian_dla_shella = 0
    gap = 1
    while gap < n:
        j = gap
        while j<n:
            i = j-gap

            while i >= 0:
                if arr[i+gap] >= arr[i]:
                        break
                else:
                    liczba_zamian_dla_shella += 1
                    arr[i+gap], arr[i] = arr[i], arr[i+gap]
                i=i-gap
            j+=1
        gap = gap * 2

    print(liczba_zamian_dla_shella)


insertion_sort(arr)
shell(array, len(array))
print(arr)
print(arr)
print(array)