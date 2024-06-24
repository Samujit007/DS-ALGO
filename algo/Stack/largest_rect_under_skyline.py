# #time: o(n*2) space o(1)
# def largestRectUnderSkyline(arr):
#     max_area = 0
#     for idx, i in enumerate(arr):
#         left_idx = idx-1
#         right_idx = idx+1
#         while idx !=0 and left_idx!=0 and arr[left_idx] >= arr[idx]:
#             left_idx -=1
#         while idx != len(arr)-1 and right_idx != len(arr) and arr[right_idx] >= arr[idx]:
#             right_idx += 1
#         width = (idx-left_idx)+(right_idx-idx)-1    
#         current_area = arr[idx] *width
#         if current_area > max_area:
#             max_area = current_area   
        
#     return max_area

# arr = [1, 3, 3, 2, 4, 1, 5, 3, 2]
# print(largestRectUnderSkyline(arr))

#time: o(n*2) space o(1)
from turtle import width


def largestRectUnderSkyline(arr):
    max_area = 0
    pillarIndices = []
    for idx, i in enumerate(arr + [0]):
        while len(pillarIndices) != 0 and arr[pillarIndices[-1]] >= i:
            pillar_height = arr[pillarIndices.pop()]
            width = idx if len(pillarIndices) == 0 else idx - pillarIndices[-1] -1
            max_area = max(width * pillar_height, max_area)
        pillarIndices.append(idx)    
    return max_area

arr = [1, 3, 3, 2, 4, 1, 5, 3, 2]
print(largestRectUnderSkyline(arr))