
def quickSort(arr):
    quickHelper(arr, 0, len(arr)-1)
    return arr

def quickHelper(arr, startIndex, endIndex):
    if startIndex >= endIndex:
        return
    pivotIndex = startIndex
    leftIndex =  startIndex + 1
    rightIndex = endIndex  
    while rightIndex >= leftIndex:
        if arr[leftIndex] > arr[pivotIndex] and arr[rightIndex] < arr[pivotIndex]:
            swap(leftIndex, rightIndex, arr)
        if arr[leftIndex] <=  arr[pivotIndex]:
            leftIndex += 1
        if arr[rightIndex] >= arr[pivotIndex]:
            rightIndex -= 1    
    swap(pivotIndex, rightIndex, arr)
    isLeftSubArrSmaller = rightIndex-1-startIndex < endIndex-(rightIndex+1)
    if isLeftSubArrSmaller:
        quickHelper(arr, startIndex, rightIndex-1)
        quickHelper(arr, rightIndex+1, endIndex)
    else:
        quickHelper(arr, rightIndex+1, endIndex)
        quickHelper(arr, startIndex, rightIndex-1)

        
def swap(leftIndex, rightIndex, arr):
    arr[leftIndex], arr[rightIndex] = arr[rightIndex], arr[leftIndex]

arr = [8, 5, 2, 9, 5, 6, 3]

print(quickSort(arr))