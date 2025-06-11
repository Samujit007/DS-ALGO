#time: o(n) space o(n)
def trapping_water(height):
    total_trapped_water = 0
    left_max = [0]*len(height)
    right_max = [0]*len(height)
    left_max[0] = height[0]# storing the max height left 
    right_max[len(height)-1] = height[len(height)-1]# storing the max height left 

    for idx in range(1, len(height)):
        left_max[idx] = max(left_max[idx-1], height[idx])
    for idx in reversed(range(len(height)-1)):
        right_max[idx] = max(right_max[idx+1], height[idx])

    for i in range(len(height)):
        h = min(left_max[i], right_max[i])-height[i]
        total_trapped_water += h
    return total_trapped_water

height = [0,1,0,2,1,0,1,3,2,1,2,1]
#[4, 2, 0, 3, 2, 5]
#[0,1,0,2,1,0,1,3,2,1,2,1]

print(trapping_water(height))#
