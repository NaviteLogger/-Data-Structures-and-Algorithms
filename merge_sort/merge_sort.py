def mergeSort(arr):
    if len(arr) > 1:
        m = len(arr) // 2
        leftArray = arr[:m]
        rightArray = arr[m:]

        mergeSort(leftArray)
        mergeSort(rightArray)

        i = j = k = 0
        while i < len(leftArray) and j < len(rightArray):
            if leftArray[i] < rightArray[j]:
                arr[k] = leftArray[i]
                i += 1
            else:
                arr[k] = rightArray[j]
                j += 1
            k += 1

        while i < len(leftArray):
            arr[k] = leftArray[i]
            i += 1
            k += 1

        while j < len(rightArray):
            arr[k] = rightArray[j]
            j += 1
            k += 1


# array = [35, 22, 41, 4, 8, 81, 15]
# mergeSort(array)
# print(array)
