#My approach
#Time o(n) space o(1)
def firstDuplicateValue(arr):
    val = 0
    str_map = {val:0}
    for i in arr:
        if i not in str_map:   
            str_map[i] = 1
            val = i
        else:
            return i
    return -1

arr =  [2, 1, 5, 2, 3, 3, 4]

print(firstDuplicateValue(arr))