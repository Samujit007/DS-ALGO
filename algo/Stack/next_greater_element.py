#Brute force TIme: O(n*2) space o(n)
def nextGreaterElement(arr):
    out = []
    for idx, i in enumerate(arr):
        if idx == len(arr)-1:
            next = 0
        else:    
            next = idx+1  
        while arr[next] <= arr[idx]:
            if next == idx:
                break 
            next += 1
            if next > (len(arr)-1):
                next = 0
        if next==idx:
            out.append(-1)
        else:      
            out.append(arr[next])     
    return out    
arr = [2, 5, -3, -4, 6, 7, 2]
print(nextGreaterElement(arr))