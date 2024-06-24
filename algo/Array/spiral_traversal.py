#My approach
#Time o(n) space o(n)
def spiralTraversal(arr):
    out = []
    start_row, end_row = 0, len(arr)-1
    start_col, end_col = 0, len(arr[0])-1

    while start_row <= end_row and start_col <= end_col:
      for i in range(start_col, end_col+1):
        out.append(arr[start_row][i])
      for i in range(start_row+1, end_row+1):
        out.append(arr[i][end_col])
      # for i in range(end_col-1, start_col-1, -1):
      #   out.append(arr[end_row][i])
      # for i in range(end_row-1, start_col, -1):
      #   out.append(arr[i][start_col])
      for i in reversed(range(start_col, end_col)):
        if start_row == end_row:
          break
        out.append(arr[end_row][i])
      for i in reversed(range(start_row+1, end_row)):
        if start_col == end_col:
          break
        out.append(arr[i][start_col])

      start_row += 1 
      end_row -= 1 
      start_col += 1
      end_col -= 1
    return out

arr = [
    [1, 2, 3, 4],
    [10, 11, 12, 5],
    [9, 8, 7, 6]
  ]

# arr = [
#   [1, 2, 3, 4],
#   [12, 13, 14, 5],
#   [11, 16, 15, 6],
#   [10, 9, 8, 7]
# ]

print(spiralTraversal(arr))