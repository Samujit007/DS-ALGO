def sort_stack(arr):    
    if len(arr) != 0:
        last_elm = arr[-1]
        arr.pop()
        sort_stack(arr)
        insert_stack(arr, last_elm)
    else:
        return arr #base case
    return arr
def insert_stack(arr, val):
    if len(arr) == 0:
       arr.append(val)
    else:
        last_elm = arr[-1] 
        if val >= last_elm:
            arr.append(val)
        else:
            arr.pop()
            insert_stack(arr, val)  
            insert_stack(arr, last_elm)  
    pass
    # while 
    # new_last = arr[last]
    # arr.pop()
    # if new_last > last: 
    #     arr.append(last)
    #     arr.append(new_last)
    # else:
    #     arr.append(new_last) 
    #     arr.append(last)   
    # return True

arr = [2, 33, 44, 2, -9, -7, -5, -2, -2, -2, 0]#[-5, 1, -3, 5, 3, 2, -6] #ans [-5, -3, 1, 3, 5] 
print("Org: ", arr)
print(sort_stack(arr))
print("Sorted: ", arr)  