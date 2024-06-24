#Time O(nlogn) space o(1)

# def taskAssignment(arr, k):
#     val_idx_map = {}
#     for idx in range(0, len(arr)):
#         val_idx_map[idx] = arr[idx]
#     s_arr = sorted(arr)
#     out = []
#     first_pointer = 0
#     last_pointer = len(s_arr) - 1
#     while first_pointer < last_pointer:
#         actual_idx_1 = [k for k, v in val_idx_map.items() if v == s_arr[first_pointer]][0]
#         val_idx_map.pop(actual_idx_1)
#         actual_idx_2 = [k for k, v in val_idx_map.items() if v == s_arr[last_pointer]][0]
#         val_idx_map.pop(actual_idx_2)
#         out.append([actual_idx_1, actual_idx_2])
#         first_pointer += 1
#         last_pointer -= 1
#         k -= 1
#         pass
#     return out  

# arr = [1, 3, 5, 3, 1, 4]
# k = 3
# print(taskAssignment(arr, k))

#=============================================================================================

def taskAssignment(arr, k):
    val_idx_map = {}
    for idx in range(0, len(arr)):
        if arr[idx] not in val_idx_map:
            val_idx_map[arr[idx]] =[idx]
        else:
            val_idx_map[arr[idx]].append(idx)    
    s_arr = sorted(arr)
    out = []
    first_pointer = 0
    last_pointer = len(s_arr) - 1
    while first_pointer < last_pointer:
        actual_idx_1 = val_idx_map[s_arr[first_pointer]].pop()
        actual_idx_2 = val_idx_map[s_arr[last_pointer]].pop()
        out.append([actual_idx_1, actual_idx_2])
        first_pointer += 1
        last_pointer -= 1
        k -= 1
        pass
    return out  

arr = [1, 3, 5, 3, 1, 4]
k = 3
print(taskAssignment(arr, k))