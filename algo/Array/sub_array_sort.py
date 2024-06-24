#My approach
#Time o(n) space o(1)

def subArraySort(arr):
    if arr == sorted(arr):
        return [-1,-1]
    indexes = []
    for idx,i in enumerate(arr):
        if idx == 0:
            if arr[idx] < arr[idx+1]:
                pass
            else:
                indexes.append(idx)
        else:
            if idx != len(arr)-1:                
                if arr[idx-1] > arr[idx] or arr[idx] > arr[idx+1]:
                    indexes.append(idx)
                    pass
            else:
                if arr[idx-1] > arr[idx]:
                    indexes.append(idx)
                    pass
            pass    
        pass 
    max_in_indexes = max([arr[i] for i in range(indexes[0], indexes[len(indexes)-1]+1)])
    min_in_indexes = min([arr[i] for i in range(indexes[0], indexes[len(indexes)-1]+1)])
    left_idx = 0
    while min_in_indexes >=arr[left_idx]:
        left_idx += 1
    right_idx = len(arr)-1
    while max_in_indexes <=arr[right_idx]:
        right_idx -= 1

    # print(left_idx, right_idx)
    return [left_idx, right_idx]
arr =  [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]

print(subArraySort(arr))