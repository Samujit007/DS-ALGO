#o(n*2^n) time and space

def powerSet(arr):
    subsets = [[]]
    for i in arr:
        for j in range(len(subsets)):
            currentSubset = subsets[j]
            subsets.append(currentSubset + [i])
    return subsets
arr = [1,2,3]
print(powerSet(arr))