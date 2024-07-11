# We are given an array asteroids of integers representing asteroids in a row.

# For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

# Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

 

# Example 1:

# Input: asteroids = [5,10,-5]
# Output: [5,10]
# Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
# Example 2:

# Input: asteroids = [8,-8]
# Output: []
# Explanation: The 8 and -8 collide exploding each other.
# Example 3:

# Input: asteroids = [10,2,-5]
# Output: [10]
# Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.

# using Stack
# def asteroid_collision(asteroids):
#     stk = [asteroids[0]] #first entry
#     for idx in range(1, len(asteroids)):
#         if stk and stk[-1] < 0:
#             stk.append(asteroids[idx])
#         elif asteroids[idx] > 0 and stk[-1] > 0:
#             stk.append(asteroids[idx])
#         elif stk[-1] > 0 and asteroids[idx] < 0:
#             sum = stk[-1] + asteroids[idx]
#             if sum == 0:
#                 stk.pop()
#                 continue
#             while stk[-1] > 0 and sum <= 0:
#                 if sum == 0:
#                     stk.pop()
#                     break
#                 stk.pop()
#                 if stk:
#                     sum = stk[-1] + asteroids[idx]
            
                        
#     return stk


def asteroid_collision(asteroids):
    stk = [asteroids[0]] #first entry
    for idx in range(1, len(asteroids)):
        while stk and stk[-1] > 0 and asteroids[idx] < 0:
            sum = stk[-1] + asteroids[idx]
            if sum < 0:
                stk.pop()
            elif sum > 0:
                asteroids[idx] = 0
                break
            else:#sum==0
                stk.pop()
                asteroids[idx] = 0
                break
        if asteroids[idx] != 0:
            stk.append(asteroids[idx])                 
    return stk
asteroids = [8,-8, -12]
#[-4, 3, 2, -2, 1]
#[10,2,7, -5, -9]
# [5,10,-5]

print(asteroid_collision(asteroids))

