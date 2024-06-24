def largestRange(arr): 
    nums = set(arr) 
    maxlength=0 
    bestRange = []

    for num in arr:
        if num - 1 not in nums:     
            i = num
            while i in nums:
                i+= 1

            currentlength =	i - num
            if	currentlength > maxlength :
                maxlength = currentlength
                bestRange  = [num , i - 1]
    return bestRange
arr = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]
print(largestRange(arr))