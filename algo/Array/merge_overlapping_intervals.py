#My approach
#Time o(n) space o(n)
def mergeOverlappingIntervals(arr):
    arr.sort()
    out = []
    current_merge = arr[0]
    for idx, i in enumerate(arr):
        if idx!=0:
            if i[0] <= current_merge[1]:
                if i[1] > current_merge[1]:
                    current_merge = [current_merge[0], max(arr[idx-1][1], arr[idx][1])]
            else:
                out.append(current_merge)
                current_merge = arr[idx]
    
    if current_merge:
        out.append(current_merge)
    return out

arr =  [
  [1, 2],
  [3, 5],
  [4, 7],
  [6, 8],
  [9, 10]
]

# arr =  [
#     [2, 3],
#     [4, 5],
#     [6, 7],
#     [8, 9],
#     [1, 10]
#   ]

# arr = [
#     [2, 3],
#     [4, 5],
#     [6, 7],
#     [8, 9],
#     [1, 10]
#   ]
# arr = [[1, 2],
#   [3, 8],
#   [9, 10]]

# arr = [
#   [1, 10],
#   [4, 5],
#   [6, 7],
#   [8, 9]
# ]

# arr = [
#     [1,4],
#     [2,3]
# ]

# arr =  [
#   [1, 2],
#   [3, 5],
#   [4, 7],
#   [6, 8],
#   [9, 10]
# ]
# arr = [[1, 3],
#     [2, 8],
#     [9, 10]]

# arr = [
#     [1, 22],
#     [-20, 30]
#   ]

print(mergeOverlappingIntervals(arr))