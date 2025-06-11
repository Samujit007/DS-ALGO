#time : o(n) spane o(1)
def trapping_water(height):
    water = 0
    max_left = height[0]
    max_right = height[-1]
    left = 0
    right = len(height)-1
    while left < right:
        if max_left < max_right:
            left += 1
            max_left = max(max_left, height[left])
            water += max_left - height[left]
        else:
            right -= 1
            max_right = max(max_right, height[right])
            water += max_right - height[right]
    return water

height = [0,1,0,2,1,0,1,3,2,1,2,1]
#[4, 2, 0, 3, 2, 5]
#[0,1,0,2,1,0,1,3,2,1,2,1]

print(trapping_water(height))
