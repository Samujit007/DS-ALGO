#o(2^( n+m))
# def numberOfDiffWaysToTraverseGraph(height, width):
#     if height == 1 or width == 1 :
#         return 1
#     return numberOfDiffWaysToTraverseGraph(height, width-1) + numberOfDiffWaysToTraverseGraph(height-1, width)     
# height = 3
# width = 4
# print(numberOfDiffWaysToTraverseGraph(height, width))


#============================================================================================

def numberOfDiffWaysToTraverseGraph(height, width):
    if height == 1 or width == 1 :
        return 1
    return numberOfDiffWaysToTraverseGraph(height, width-1) + numberOfDiffWaysToTraverseGraph(height-1, width)     
height = 3
width = 4
print(numberOfDiffWaysToTraverseGraph(height, width))