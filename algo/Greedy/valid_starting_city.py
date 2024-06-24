#Time o(n^2) space o(1)
# def validStartingCity(dist, fuel, mpg):
#     total_dist = sum(dist)
#     for idx in range(0, len(dist)):
#         travel_capacity = fuel[idx] * mpg
#         if dist[idx] < travel_capacity :
#             remaining_fuel = travel_capacity - dist[idx]
#             remaining_dist = total_dist - dist[idx]
#             counter = idx+1 if idx != len(dist) - 1 else 0
#             while remaining_dist !=0 and counter < len(dist) :
#                 travel_capacity = remaining_fuel + fuel[counter] * mpg
#                 remaining_fuel = travel_capacity - dist[counter]
#                 if dist[counter] > travel_capacity:
#                     break
#                 remaining_dist -= dist[counter]
#                 # counter += 1
#                 counter = counter+1 if counter != len(dist) - 1 else 0
#             if remaining_dist == 0:
#                 return idx 

# dist = [5, 25, 15, 10, 15]
# fuel = [1, 2, 1, 0, 3]
# mpg = 10
# print(validStartingCity(dist, fuel, mpg))

#=============================================================

def validStartingCity(dist, fuel, mpg):
    remaing_fuel = 0
    miles_left = sum(dist)
    less_fuel = 0
    valid_city_index = 0
    for idx in range(1, len(dist)):
        remaing_fuel += fuel[idx-1]*mpg - dist[idx-1]
        miles_left -=  dist[idx-1]
        if remaing_fuel < less_fuel:
            less_fuel = remaing_fuel
            valid_city_index = idx
    return valid_city_index

dist = [30, 40, 10, 10, 17, 13, 50, 30, 10, 40]#[5, 25, 15, 10, 15]
fuel = [10, 0, 0, 0, 0, 0, 0, 0, 0, 0]#[1, 2, 1, 0, 3]
mpg = 25#10
print(validStartingCity(dist, fuel, mpg))