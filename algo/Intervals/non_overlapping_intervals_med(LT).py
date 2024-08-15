def non_overlapping_intervals(intervals):
    if len(intervals) == 1:
         return 0
    intervals.sort()#nlogn
    count = 0
    pointer1 = 0
    pointer2 = 1
    while pointer2 < len(intervals):
        if intervals[pointer2][0] < intervals[pointer1][1]: 
            count += 1
            if intervals[pointer2][1] >= intervals[pointer1][1]:     
                pointer2 += 1
            else:
                pointer1 = pointer2
                pointer2 += 1
        else:
            pointer1 = pointer2
            pointer2 += 1
            
    return count

intervals = [[-52,31],[-73,-26],[82,97],[-65,-11],[-62,-49],[95,99],[58,95],[-31,49],[66,98],[-63,2],[30,47],[-40,-26]]

#[[0,2],[1,3],[2,4],[3,5],[4,6]]#[[1,2],[2,3],[3,4],[1,3]]##[[0,2],[1,3],[2,4],[3,5],[4,6]]#[[1,2],[2,3],[3,4],[1,3]]#[[1,2],[1,2],[1,2]]#[[1,2],[2,3]]#[[1,100],[11,22],[1,11],[2,12]]
#[[1,2],[2,3]]#[[1,2],[1,2],[1,2]]# [[1,2],[2,3],[3,4],[1,3]]
# [[2, 3], [1, 3]]
print(non_overlapping_intervals(intervals))
#approach 1 .. but not passing all the test cases
# def non_overlapping_intervals(intervals):
#     if len(intervals) == 1:
#          return 0
#     low = intervals[0][0]
#     high = intervals[0][1]
#     count = 0
#     for idx, i in enumerate(intervals):
#         if idx != 0:
#             if i[0] <= low: 
#                 # if i[1] >= high:
#                 low = i[0]
#                 #     high = i[1]
#                 count += 1
#                 # else:
#                 #     pass
#             if i[1] > high:
#                     high = i[1]
#     return count

# intervals = [[1,100],[11,22],[1,11],[2,12]]
# #[[1,2],[2,3]]#[[1,2],[1,2],[1,2]]# [[1,2],[2,3],[3,4],[1,3]]
# # [[2, 3], [1, 3]]
# print(non_overlapping_intervals(intervals))