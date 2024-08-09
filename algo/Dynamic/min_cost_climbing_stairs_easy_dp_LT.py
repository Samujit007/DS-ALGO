#simple approach
def min_cost_climbing_stairs(cost):
    cost.append(0)
    for idx in range(len(cost)-3, -1, -1):
        cost[idx] += min(cost[idx+1], cost[idx+2])
        pass
    return min(cost[0], cost[1])

cost = [1,100,1,1,1,100,1,1,100,1]
#[1,100,1,1,1,100,1,1,100,1]
print(min_cost_climbing_stairs(cost))

#===========================================
#recursion|without Memoization|Google
# cost = [10,15,20]
# def availability_check(i):
#     if i >= len(cost):
#         return 0 
#     a = cost[i] + availability_check(i+1)
#     b = cost[i] + availability_check(i+2)
#     return min(a, b)


# def min_cost_climbing_stairs(cost):
#     return min(availability_check(0), availability_check(1))


# #[1,100,1,1,1,100,1,1,100,1]
# print(min_cost_climbing_stairs(cost))



# Try=======================================================
# def availability_check(step1, step2):
#     lowest_cost_step = float("-inf")
#     # incoming_step1 = + 
#     if step1 < step2:
#         lowest_cost_step = min(lowest_cost_step, step1)
#     else:
#         lowest_cost_step = min(lowest_cost_step, step2)

    
#     return lowest_cost_step


# def min_cost_climbing_stairs(cost):
#     #base
#     if len(cost)==1:
#         return cost[0]
    
#     step1 = min(cost[0], cost[1])
#     min_cost = step1
#     step2 = step1 + 1
    
#     while step2 < len(cost): #o(n)
#         if cost[jdx] < cost[idx]:
#             jump_from = jdx
#         else:
#             jump_from = idx
#     return min_cost

# cost = [10,15,20]
# #[1,100,1,1,1,100,1,1,100,1]
# print(min_cost_climbing_stairs(cost))