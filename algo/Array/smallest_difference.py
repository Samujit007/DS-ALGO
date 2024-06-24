#myapproach
#Time o(n^2) space o(n)

# def smallestDifference(arr1, arr2):
#     if len(arr1) == len(arr2) == 1:
#         return [arr1[0],arr2[0]]
#     closest_val = float('inf')
#     pair = {closest_val:[]}
#     for i in arr1:
#         for j in arr2:
#             if abs(i-j)==0:
#                 return [i, j]
#             else:
#                 diff = abs(i-j)
#                 if diff < closest_val:
#                     closest_val = diff
#                     pair[closest_val] = [i, j]

#     return pair[closest_val]

# arr1 = [-1, 5, 10, 20, 28, 3]
# arr2 = [26, 134, 135, 15, 17]

# print(smallestDifference(arr1, arr2))

#======================================================
#Time o(nlog(n) + mlog(m)) space o(1)
def smallestDifference(arr1, arr2):
    if len(arr1) == len(arr2) == 1:
        return [arr1[0],arr2[0]]
    arr1.sort()
    arr2.sort()
    first_pointer = 0
    second_pointer = 0
    closest_diff = float('inf')
    petential_out = []
    while first_pointer < len(arr1) and second_pointer < len(arr2):
        if arr1[first_pointer] == arr2[second_pointer]: #base case
            return [arr1[first_pointer],arr2[second_pointer]]

        if arr1[first_pointer] < arr2[second_pointer]:
            diff = abs(arr1[first_pointer]-arr2[second_pointer])
            if diff < closest_diff:
                petential_out = [arr1[first_pointer],arr2[second_pointer]] 
                closest_diff = diff
            first_pointer += 1  
        else:
            diff = abs(arr1[first_pointer]-arr2[second_pointer])
            if diff < closest_diff:              
                petential_out = [arr1[first_pointer],arr2[second_pointer]]
                closest_diff = diff 
            second_pointer += 1
  
    return petential_out

arr1 = [-1, 5, 10, 20, 28, 3]#[-1, 5, 10, 20, 3]
arr2 = [26, 134, 135, 15, 17]#[26, 134, 135, 15, 17,-1]#

print(smallestDifference(arr1, arr2))


