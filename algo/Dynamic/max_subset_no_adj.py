# maxsum[i] = max(maxsum[i-1], maxsum[i-2] + arr[i])
#Time o(n) |Space o(n)
# def maxSub(arr):
#     maxsum = []
#     if len(arr) == 0:
#         return 0
#     for i, j in enumerate(arr):
#         if i==0:
#             maxsum.append(j)
#         elif i ==1:
#             if maxsum[0] > j:
#                maxsum.append(maxsum[0]) 
#             else:
#                maxsum.append(j)       
#         else:
#             last_max_sum = maxsum[i-1]
#             second_last_max_sum =  maxsum[i-2]
#             if last_max_sum > second_last_max_sum + j:
#                 maxsum.append(last_max_sum)
#             else:
#                 maxsum.append(second_last_max_sum + j)             
#     return maxsum[-1]

# arr = [10, 3, 67, 98, 21, 43]
# print(maxSub(arr))
#Time o(n) |Space o(1)
def maxSub(arr):
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return arr[0]  
    first_max = arr[0]
    scnd_max =  max(arr[0], arr[1])   
    for i, j in enumerate(arr):
        if i>1:
            if scnd_max < first_max + j:
                scnd_max, first_max = first_max+j, scnd_max
            else:
                scnd_max, first_max = scnd_max, scnd_max
    return scnd_max

arr = [10, 3, 67, 98, 21, 43]
print(maxSub(arr))