#Time O(N) space o(1)
def searchInSortedMatrix(arr, target):
    right_col_idx = len(arr[0])-1
    start_row = 0
    while right_col_idx !=-1 and start_row != len(arr):
        if target == arr[start_row][right_col_idx]:
            return [start_row, right_col_idx]
        if target < arr[start_row][right_col_idx]:
            right_col_idx -=1
            while target < arr[start_row][right_col_idx]:
                right_col_idx -= 1 
                if right_col_idx == -1: 
                    break 
            if target == arr[start_row][right_col_idx]:
                return [start_row, right_col_idx]     
            # start_row +=1    
        else:
            start_row +=1
            while target > arr[start_row][right_col_idx]: 
                start_row +=1  
                if start_row == len(arr)-1: 
                    break
            if target == arr[start_row][right_col_idx]:
                return [start_row, right_col_idx]    
            # right_col_idx -=1          
    return [-1,-1]  


arr = [
  [1, 4, 7, 12, 15, 1000],
  [2, 5, 19, 31, 32, 1001],
  [3, 8, 24, 33, 35, 1002],
  [40, 41, 42, 44, 45, 1003],
  [99, 100, 103, 106, 128, 1004]
]
target = 99
print(searchInSortedMatrix(arr,target))