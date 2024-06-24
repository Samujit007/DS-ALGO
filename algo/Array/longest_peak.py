#My approach
#Time o(n) space o(1)
# def longestPeak(arr):
#     peak_hight = ""
#     ground_idx = 0
#     map_t = {}#{"0|4":5}
#     patt = "" 
#     for idx, i in enumerate(arr):
#         if idx != 0:
#             diff = arr[idx] - arr[idx-1]
#             if diff == 0 :
#                 patt =""
#                 ground_idx +=1
#                 pass
#             elif diff > 0 :
#                 if patt == "decr-incr":
#                     ground_idx = idx-1 
#                 patt = "incr"
#             elif diff < 0 :
#                 if patt !="":  
#                     peak_hight = max([arr[i] for i in range(ground_idx, idx)])
#                     map_t[peak_hight] = idx - ground_idx +1
#                 if patt == "incr":
#                     patt = "incr-decr"
#                 if patt == "decr":
#                     patt = "decr-decr"
#                 if idx != len(arr)-1:
#                     if arr[idx] < arr[idx+1]:
#                         patt = "decr-incr"
#     print("map_t: ", map_t)
#     return  0 if len(map_t) == 0 else map_t[max(map_t)]

# arr = [1, 1, 1, 2, 3, 10, 12, -3, -3, 2, 3, 45, 800, 99, 98, 0, -1, -1, 2, 3, 4, 5, 0, -1, -1] 
# #[1, 1, 3, 2, 1]#[1, 2, 3, 3, 2, 1]#[5, 4, 3, 2, 1, 2, 1]#[1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]

# print(longestPeak(arr))

#==============================================
#Time o(n) space o(1)
def longestPeak(arr):
    peak_length = 0
    peak = 0
    for idx, i in enumerate(arr):
        if idx != 0 and idx!= len(arr)-1:
            if arr[idx-1] < arr[idx] and arr[idx] > arr[idx+1]:
                peak_temp = arr[idx]
                left_slope = idx-1
                right_slope = idx+1
                if left_slope != 0:
                    while arr[left_slope] > arr[left_slope-1]:
                        left_slope -=1
                if right_slope!=len(arr)-1:
                    while arr[right_slope+1] < arr[right_slope]:    
                        right_slope +=1
                        if right_slope == len(arr)-1:
                            break
                if peak_temp>peak:
                    peak = peak_temp
                    peak_length = right_slope-left_slope+1
    return peak_length            

arr = [1, 1, 3, 2, 1]#[1, 3, 2]#[1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]

print(longestPeak(arr))