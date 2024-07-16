def containter_with_most_water(height):
    max_area = 0
    max_left_bar = 0
    max_right_bar = len(height)-1
    while max_right_bar-max_left_bar > 0 :
        container_length = max_right_bar-max_left_bar
        container_height = min(height[max_left_bar], height[max_right_bar])
        area = container_length*container_height
        if area > max_area:
            max_area = area
        if height[max_left_bar] < height[max_right_bar]:
            max_left_bar += 1
        else:
            max_right_bar -= 1
    return max_area



height = [1,8,6,2,5,4,8,3,7]

print(containter_with_most_water(height))




# def containter_with_most_water(height):
#     l = 0
#     r = len(height)
#     max_area = 0
#     max_left_bar = 0
#     max_right_bar = len(height)
#     while l<r:
#         container_length = max_right_bar-1-max_left_bar
#         container_height = min(height[max_left_bar], height[max_right_bar-1])
#         area = container_length*container_height
#         if area > max_area:
#             max_area = area
#         l += 1
#         r -= 1
#         if l > max_left_bar:
#             max_left_bar = l
#         if r > max_right_bar:
#             max_right_bar = r    
#     return max_area



# height = [2,3,4,5,18,17,6]#[1,8,6,2,5,4,8,3,7]

# print(containter_with_most_water(height))

