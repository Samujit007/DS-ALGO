import heapq
def kth_largest(nums, k):
    min_heap = []
    for num in nums:
        if len(min_heap) < k:
            heapq.heappush(min_heap, num)
        else:
            if num > min_heap[0]:
                heapq.heappushpop(min_heap, num)
    return min_heap[0]
nums = [3,2,1,5,6,4]
k = 2

print(kth_largest(nums, k))


#not good time exceeds

# def arrange_min_heap(min_heap):
#     min_heap.sort(reverse=True)
#     return min_heap

# def kth_largest(nums, k):
#     min_heap = []
#     for idx in range(len(nums)):
#         if len(min_heap) < k:
#             min_heap.append(nums[idx])
#             min_heap = arrange_min_heap(min_heap)
#         else:
#             last_ele = min_heap[-1]
#             if nums[idx]>last_ele: 
#                 min_heap.pop()    
#                 min_heap.append(nums[idx])
#                 min_heap = arrange_min_heap(min_heap)
#     return min_heap.pop()
# nums = [3,2,1,5,6,4]
# k = 2

# print(kth_largest(nums, k))


#Time: o(nlogn) + o(k)
# def kth_largest(nums, k):
#     nums.sort()#o(nlogn)
#     res = None
#     for i in range(len(nums)-1, len(nums)-k-1, -1):#o(k)
#         res = nums[i]
#     return res


# nums = [3,2,3,1,2,4,5,5,6]
# k = 4

# print(kth_largest(nums, k))