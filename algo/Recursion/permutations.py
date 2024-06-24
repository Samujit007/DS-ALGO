def permutations(arr):
    out = []
    helper(0, arr, out)
    return out
def helper(i, arr, out):
    if i==len(arr)-1:
        out.append(arr[:])
    else:
        for j in range(i, len(arr)):
            arr[i], arr[j] = arr[j], arr[i]
            helper(i+1,arr, out)
            arr[i], arr[j] = arr[j], arr[i]
            pass

arr = [1, 2, 3, 4]

print(permutations(arr))