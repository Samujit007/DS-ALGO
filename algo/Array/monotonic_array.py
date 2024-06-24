#My approach
#Time o(n) space o(1)
def monotonicArray(arr):
    if len(arr) == 0 or len(arr) == 1:
        return True
    pat = ""
    for idx, i in enumerate(arr):
        if idx != 0:
            diff = arr[idx] - arr[idx-1] 
            if diff == 0:
                pass
            elif diff > 0:
                if pat=="decr":
                    return False 
                pat = "incr"
            elif diff < 0 :
                if pat=="incr":
                    return False 
                pat = "decr"    
    return True   

arr =  [-1, -5,-10, -1100, -1100, -1101, -1102, -9001]

print(monotonicArray(arr))