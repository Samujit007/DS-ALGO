# Increasing Triplet Subsequence
# Medium
# Topics
# Companies
# Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

 

# Example 1:

# Input: nums = [1,2,3,4,5]
# Output: true
# Explanation: Any triplet where i < j < k is valid.
# Example 2:

# Input: nums = [5,4,3,2,1]
# Output: false
# Explanation: No triplet exists.
# Example 3:

# Input: nums = [2,1,5,0,4,6]
# Output: true
# Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.


#======================o(n) time and space considering triplets are adjacent====================
# def increasing_triplet_subsequence(nums):

#     triplet = 3
#     i = 0
#     j = 1
#     i_temp=0
#     length = len(nums)-1
#     while j <= length:
#         if j - i == triplet:
#             return True
#         if nums[j] > nums[i_temp] and j-i+1 <= triplet:
#             i_temp += 1
#             j += 1
#         else:
#             i = j
#             i_temp = i
#             j += 1    
#     return j - i == triplet

# nums = [5,4,3,2,1]#[1,2,3,4,5]
# #[5,4,3,2,1]
# #[2,1,5,0,4,6]
# print(increasing_triplet_subsequence(nums))
#==============================================================================================

def increasing_triplet_subsequence(nums):
    num1=float('inf')
    num2=float('inf')
    idx_num3 = 0
    length = len(nums)-1

    while idx_num3 <= length:
        if nums[idx_num3] <= num1:
            num1 = nums[idx_num3]
        elif nums[idx_num3] <= num2:
            num2= nums[idx_num3]    
        else:
            return True
        idx_num3 += 1    
    return False

nums = [2,1,5,0,4,6]#[5,4,3,2,1]#[20,100,10,12,5,13]
# [5,4,3,2,1]#[1,2,3,4,5]
#[5,4,3,2,1]
#[2,1,5,0,4,6]
print(increasing_triplet_subsequence(nums))