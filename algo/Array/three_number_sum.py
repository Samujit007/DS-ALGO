# #time: o(n^3) space o(1)

# def threeNumberSum(arr, target):
#     out = []
#     for i in arr:
#         for j in arr:
#             for k in arr:
#                 sum = float('inf')
#                 if i!=j!=k:
#                     sum = i+j+k
#                 if sum == target:
#                     if i<j<k:
#                         out.append([i,j,k])      
#         # remaining_sum = target - i
#         # if remaining_sum in sum_map:
#         #     pass
#         # else:
            
#         #     pass
#         # pass
#     print(out)
# arr = [12, 3, 1, 2, -6, 5, -8, 6]
# target = 0

# threeNumberSum(arr, target)

#=============================Sorting techin==========================================
#time: o(n^2) space o(1)

def threeNumberSum(arr, target):
    out = []
    arr.sort()
    for idx, i in enumerate(arr):
        left_counter = idx+1
        right_counter = len(arr) -1
        for jdx,j in enumerate(arr[idx+1:-1]):
            if left_counter > right_counter:
                break
            sum = i + arr[left_counter] + arr[right_counter]
            if sum == target:
                if i != arr[left_counter] != arr[right_counter]:
                    out.append([i, arr[left_counter], arr[right_counter]])
                left_counter += 1
                right_counter -= 1
            elif sum < target:
                left_counter += 1
            elif sum > target:
                right_counter -= 1 

    print(out)
        

    

arr = [12, 3, 1, 2, -6, 5, -8, 6]
target = 0

threeNumberSum(arr, target)