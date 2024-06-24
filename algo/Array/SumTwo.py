#=O(n2) space O(1)=
# def twoNumberSum(array, targetSum):
#     for num1 in array:
#         for num2 in array:
#             sum = 0
#             if num1 != num2:
#                 sum = num1+num2
#             if sum==targetSum:
#                 return [num1, num2]			
#     return []
    
# a = [3, 5, -4, 8, 11, 1, -1, 6]
# sum = 10
# print(twoNumberSum(a, sum))

#========O(n) space O(n)======================dict concept
def twoNumberSum(array, targetSum):
    # Write your code here.
	nums = {} #to store
	for num in array:
		predicted_second_num = targetSum - num
		if predicted_second_num in nums:
			return [predicted_second_num, num] 
		else:
			nums[num] = True
	return []		
a = [7, 14]#[3, 5, -4, 8, 11, 1, -1, 6]
sum = 300#10
print(twoNumberSum(a, sum))