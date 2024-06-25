# Given an integer array nums, return the length of the longest strictly increasing 
# subsequence
# .

 

# Example 1:

# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
# Example 2:

# Input: nums = [0,1,0,3,2,3]
# Output: 4
# Example 3:

# Input: nums = [7,7,7,7,7,7,7]
# Output: 1
# gen approadch
# def longest_increasing_subsequence(nums):
#     if not nums:
#         return 0
    
#     n = len(nums)
#     # dp[i] represents the length of the longest increasing subsequence that ends with nums[i]
#     dp = [1] * n

#     for i in range(1, n):
#         for j in range(0, i):
#             if nums[i] > nums[j]:
#                 dp[i] = max(dp[i], dp[j] + 1)
    
#     # The length of the longest increasing subsequence will be the maximum value in dp
#     return max(dp)

# nums = [10, 9, 2, 5, 3, 7, 101, 18


def solve(nums, current_index, prev_index, mem):
    if current_index >= len(nums):
        return 0
    if prev_index != -1 and mem[current_index][prev_index] != -1:
        return mem[current_index][prev_index]
    # take current_index
    take = 0
    if prev_index == -1 or nums[prev_index] < nums[current_index]:
        take = 1 + solve(nums, current_index+1, current_index, mem)
    # skip current_index    
    skip = solve(nums, current_index+1, prev_index, mem)
    if prev_index != -1:
        mem[current_index][prev_index] = max(take, skip)
    return max(take, skip)

def longest_increasing_subsequence(nums):
    n = len(nums)
    mem = [[-1 for _ in range(n)] for _ in range(n)]
    prev_index = -1 # default
    current_index = 0
    return solve(nums, current_index, prev_index, mem)

nums = [10,9,2,5,3,7,101,18]

print(longest_common_sunbsequence(nums))