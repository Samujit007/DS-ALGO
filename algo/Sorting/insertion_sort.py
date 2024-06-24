from enum import EnumMeta


#Time O(N^2) and Space O(1)
def insersionSort(arr):
    for idx in range(0, len(arr)-1):
        first = idx
        second = idx+1
        while first >= 0 and arr[first] > arr[second]:
            arr[first], arr[second] = arr[second], arr[first]
            first -= 1
            second -= 1
    return arr

arr = [8, 5, 2, 9, 5, 6, 3]

print(insersionSort(arr))