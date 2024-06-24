#Time: o(nlogn) for sorting and o(N) for loop rather(o(n^2)) , space  o(1) 

# def minimumWaitingTime(arr):
#     sorted_arr = sorted(arr)
#     min_time = 0
#     for idx in range(1, len(sorted_arr)):
#         each_level_time = sorted_arr[idx-1]
#         prev_idx = idx-1
#         while prev_idx !=0:
#             prev_idx -= 1
#             each_level_time += sorted_arr[prev_idx] 
#         min_time += each_level_time

#     return min_time

# arr = [3, 2, 1, 2, 6] # [1,2,3,3,6] 

# print(minimumWaitingTime(arr))

#=========================================================


def minimumWaitingTime(arr):
    sorted_arr = sorted(arr)
    min_time = 0
    for idx in range(0, len(sorted_arr)):
        level_time = sorted_arr[idx] * (len(sorted_arr)-idx-1)
        min_time += level_time

    return min_time

arr = [3, 2, 1, 2, 6] # [1,2,3,3,6] 

print(minimumWaitingTime(arr))