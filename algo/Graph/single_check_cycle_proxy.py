def singleCycleCheck(arr):
    elementVisitedNum = 0
    currentIdx = 0
    while elementVisitedNum < len(arr):
        if elementVisitedNum > 0 and currentIdx ==0:
            return False
        elementVisitedNum += 1    
        currentIdx = getNextIndex(currentIdx, arr)
    return currentIdx == 0


def getNextIndex(currentIdx, arr):
    jump = arr[currentIdx]
    nextIndex = (currentIdx + jump) % len(arr)
    return nextIndex if nextIndex >= 0 else nextIndex + len(arr)


arr = [2, 3, 1, -4, -4, 2]
print(singleCycleCheck(arr))