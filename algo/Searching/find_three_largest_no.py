#Time O(N) space o(1)
def findThreeLargestNo(arr):
    large_1 = large_2 = large_3 = -float('inf')
    for idx, i in enumerate(arr):
        if large_3 <= large_2 <= large_1 <= i:
            large_3 = large_2
            large_2 = large_1 
            large_1 = i            
        elif large_3 <= large_2 <= i <= large_1:
            large_3 = large_2
            large_2 = i
        elif  large_3 <= i <= large_2 <= large_1:
            large_3 = i    
    return [large_3, large_2, large_1]   


arr = [-1, -2, -3, -7, -17, -27, -18, -541, -8, -7, 7]
#[141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
print(findThreeLargestNo(arr))