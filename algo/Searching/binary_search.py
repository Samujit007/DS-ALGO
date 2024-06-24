#Time: o(log(N)) space o(1)
def binarySearch(arr, target):
    left = 0
    right = len(arr)-1
    while left <= right:
        if arr[left]==target:
            return left
        if arr[right] == target:
            return right    
        mid = (left + right)//2
        if target == arr[mid]:
            return mid
        elif target < arr[mid]:
            right = mid-1
        else:
            left = mid + 1    
    return -1    
arr = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
target = 73

print(binarySearch(arr, target))