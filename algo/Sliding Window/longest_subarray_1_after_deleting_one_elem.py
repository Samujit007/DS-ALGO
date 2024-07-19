# Given a binary array nums, you should delete one element from it.

# Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

 

# Example 1:

# Input: nums = [1,1,0,1]
# Output: 3
# Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
# Example 2:

# Input: nums = [0,1,1,1,0,1,1,0,1]
# Output: 5
# Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
# Example 3:

# Input: nums = [1,1,1]
# Output: 2
# Explanation: You must delete one element.


#sliding window approach
def longest_subarray_1_after_deleting_one_elem(nums):
    longest_ones = 0
    i = 0
    j = 0
    sub_window_ones = 0
    window_zero_count = 0
    while j < len(nums):
        if window_zero_count < 2:
            if nums[j] != 1:
                window_zero_count += 1 
            else:
                sub_window_ones += 1    
            j += 1  
        else:  
            longest_ones = max(longest_ones, sub_window_ones)
            while window_zero_count >= 2:
                if nums[i]!=1:
                    window_zero_count -= 1
                else:
                    sub_window_ones -=1
                i += 1
    if window_zero_count == 0:
        return sub_window_ones - 1
    return max(longest_ones, sub_window_ones)


nums = [0,1,1,1,0,0,1,1,0]
#[0,1,1,1,0,0,1,1,0]#
# [1,1,0,1]
print(longest_subarray_1_after_deleting_one_elem(nums))
