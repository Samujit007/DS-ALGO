#Story: Cannot rob the adjacency house
#Hence i can be stealed or can be skipped
#initialize a final collection array with one extra index
# [0, 2, -1, -1, -1, -1] for ex: nums = [2,7,9,3,1]
#can only steal current and prev-prev collection
#orskip current and take the last collection 
def house_robber_bottom_up(nums):
    if len(nums) == 1:
        return nums[0]
    money_collected_arr = [0]*(len(nums)+1)
    money_collected_arr[1] = nums[0]
    for idx in range(2, len(money_collected_arr)):
        steal = nums[idx - 1] + money_collected_arr[idx-2]# cannot take adjacent collection
        skip = money_collected_arr[idx-1]
        money_collected_arr[idx] = max(steal, skip)
    return money_collected_arr[len(nums)]
    

nums = [2,7,9,3,1]
print(house_robber_bottom_up(nums))



#new approach
# def house_robber_rec(nums, i, DP):
#     if i >= len(nums):
#         return 0
#     if DP[i] != -1:
#         return DP[i]
#     steal = nums[i] + house_robber_rec(nums, i+2, DP)
#     skip = house_robber_rec(nums, i+1, DP)
#     DP[i] = max(steal, skip)
#     return DP[i]
    

# nums = [1,2,3,1]
# DP = [-1]*(len(nums)+1)
# print(house_robber_rec(nums, 0, DP))




# #new approach
# def house_robber(nums):
#     idx = 0
#     sum_odd = 0
#     sum_even = 0
#     for idx, i in enumerate(nums):  
#         if idx % 2 != 0:
#             sum_odd += nums[idx]
#         else:
#             sum_even += nums[idx]    
#     return max(sum_odd, sum_even)

# nums = [1,2,3,1]
# print(house_robber(nums))

# #Partially worked but failed for edge cases
# # [2, 1, 1, 2] out: 3 but expected: 4
# def house_robber(nums):
#     idx = 0
#     sum_odd = 0
#     sum_even = 0
#     for idx, i in enumerate(nums):  
#         if idx % 2 != 0:
#             sum_odd += nums[idx]
#         else:
#             sum_even += nums[idx]    
#     return max(sum_odd, sum_even)

# nums = [1,2,3,1]

# print(house_robber(nums))