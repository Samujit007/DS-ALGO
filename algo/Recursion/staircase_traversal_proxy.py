def staircaseTraversal(height, maxSteps):
    return noOfWaysToTop(height, maxSteps)


def noOfWaysToTop(height, maxSteps):
    if height <= 1:
        return 1
    numberOfWays = 0    
    for step in range(1, min(maxSteps, height)+1):
        numberOfWays += noOfWaysToTop(height - step, maxSteps)
    return numberOfWays


height = 4
maxSteps = 2
print(staircaseTraversal(height, maxSteps))