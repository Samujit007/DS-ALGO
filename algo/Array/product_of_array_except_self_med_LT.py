#o (n)
def product_of_array_except_self(nums):
    res = [1]*len(nums)
    prefix = []
    postfix = [1]*len(nums)
    for idx, num in enumerate(nums):
        if idx == 0:
            prefix.append(num)
        else:
            prefix.append(prefix[idx-1]*num)    
    for idx in range(len(nums)-1, -1, -1): #reversed
        if idx == len(nums)-1:
            postfix[idx] = nums[idx]
        else:
            postfix[idx] = nums[idx]*postfix[idx+1] 
    for idx in range(len(nums)):
        res[idx] = (prefix[idx-1] if idx !=0 else 1) * (postfix[idx+1] if idx !=len(nums)-1 else 1)
    return res

nums = [1,2,3,4]
#[-1,1,0,-3,3]#

print(product_of_array_except_self(nums))

#time o(n^2) all test didn't pass
# def product_of_array_except_self(nums):
#     # pointer, last_elm = 0, len(nums)-1
#     res = []
#     for idx, num in enumerate(nums):
#         temp_prod = 1
#         for idxj, j in enumerate(nums):
#             if idx!=idxj:
#                 temp_prod *= nums[idxj]
#         res.append(temp_prod)
#     return res

# nums = [-1,1,0,-3,3]#

# print(product_of_array_except_self(nums))