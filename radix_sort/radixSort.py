#array = [170,  45, 75, 90, 802, 24,2,66] porównywanie jedności
#array = [170, 90, 802,02,24,45,75,66] porównywanie dziesiątek
#array = [802,002,024,045,066,170,075,090] #porównanie setek
#array = [2, 24,45,66,75,90,170,802]

def countingSort(arr,exp1):
    n =  len(arr)
    output = [0]*n
    count = [0]*10
    for i in range(0,n):
        index = arr[i]//exp1
        count[index%10] += 1
    for i in range(1,10):
        count[i]  += count[i-1]

    i = n-1
    while i>= 0:
        index = arr[i]//exp1
        output[count[index%10]-1]=arr[i]
        count[index%10]-= 1
        i-=1
    i=0
    for i in range(0,n):
        arr[i] = output[i]

def radixSort(arr):
    max1 = max(arr)
    exp =1
    while max1//exp >=1:
        countingSort(arr,exp)
        exp*=10

array = [170, 90, 802,2,24,45,75,66]
radixSort(array)
print(array)