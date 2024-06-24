#Time O(N^2) Space O(1)

def bubbleSort(arr):
    first = 0
    last = len(arr)-1
    while first != last:
        for idx in range(first, last):
            if arr[idx] > arr[idx+1]:
                arr[idx], arr[idx+1] = arr[idx+1], arr[idx]
        last -= 1           
    return arr

arr =  [8, 5, 2, 9, 5, 6, 3]#[2,1]
 
#[8, 5, 2, 9, 5, 6, 3]

print(bubbleSort(arr))