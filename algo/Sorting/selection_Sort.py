#Time O(N^2) and Space O(1)  # Most performent, better then bubble and insertion but worst than quick, merge and heap sort
def selectionSort(arr):
    
    for idx in range(0, len(arr)-1):
        small_pointer = idx
        counter = idx+1
        while counter != len(arr):
            if arr[counter] < arr[small_pointer]:
                small_pointer = counter
            counter +=1    
        arr[idx], arr[small_pointer] = arr[small_pointer], arr[idx]

    return arr

arr = [8, 5, 2, 9, 5, 6, 3]

print(selectionSort(arr))