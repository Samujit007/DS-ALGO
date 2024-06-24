def radixSort(arr):
    if len(arr) == 0:
        return arr
    maxNumber = max(arr)
    digit = 0
    while maxNumber / (10 ** digit) > 0:
        countingSort(arr, digit)
        digit += 1

    return arr

def countingSort(arr, digit):
    sortedArr = [0] * len(arr)
    countArr = [0] * 10
    digitCol = 10 ** digit

    for i in arr:
        countIdx = (i // digitCol) % 10
        countArr[countIdx] += 1
    for idx in range(1, 10):
        countArr[idx] += countArr[idx-1]

    for idx in range(len(arr) -1, -1, -1):
        countIdx = (arr[idx]//digitCol) % 10
        countArr[countIdx] -=1
        sortedIdx = countArr[countIdx]
        sortedArr[sortedIdx] = arr[idx]


    for idx in range(len(arr)):
        arr[idx] = sortedArr[idx]


arr = [8762, 654, 3008, 345, 87, 65, 234, 12, 2]

print(radixSort(arr))