def can_place_flowers(flowerbed, n):
    flowerbed = [0] + flowerbed + [0]
    for idx in range(1, len(flowerbed)-1):
        if flowerbed[idx] == 0 and flowerbed[idx-1] == 0 and flowerbed[idx+1]==0:
            n -= 1
            flowerbed[idx] = 1
    return n<=0        

flowerbed = [0,0,0]#[0,1,0,1,0,1,0,0]#[1,0,0,0,0,1]
n = 2

print(can_place_flowers(flowerbed, n))

# def can_place_flowers(flowerbed, n):
#     length_flower = len(flowerbed)
#     if n==0:
#          return True 
#     available_pos = 0
#     if flowerbed[0]==1:
#         available_pos = 2
#     elif length_flower > 1 and flowerbed[1]==1:
#         available_pos = 3    
#     while n > 0 and available_pos<=length_flower-1:
#         if flowerbed[available_pos]==0:
#             if available_pos != 0:
#                 if flowerbed[available_pos-1]==0:
#                     if available_pos == length_flower-1:
#                         n -= 1    
#                     elif flowerbed[available_pos+1]==0: 
#                         n -= 1 
#             else:
#                 if available_pos == length_flower-1:
#                         n -= 1    
#                 elif flowerbed[available_pos+1]==0: 
#                         n -= 1            
#         available_pos +=2    
#     if n>0:
#         return False
#     else:
#         return True
# flowerbed = [0,1,0,1,0,1,0,0]#[1,0,0,0,0,1]
# n = 1#2

# print(can_place_flowers(flowerbed, n))

# def can_place_flowers(flowerbed, n):
#     length_flower = len(flowerbed)
#     if flowerbed[0]==1:
#         available_pos = 2
#     else:
#         available_pos = 0
#     while n > 0 and available_pos < length_flower:
#         if flowerbed[available_pos]==0:
#             n -= 1
#         available_pos += 2

#     if n>0:
#         return False
#     if available_pos < (length_flower-1):#last_index check
#         return True
#     elif available_pos == length_flower and flowerbed[-1]==1:
#         return False
#     else:
#         return True

# flowerbed = [0,1,0]#[0,0,1,0,1]#[1,0,0,0,0,1]
# n = 1

# print(can_place_flowers(flowerbed, n))


# def can_place_flowers(flowerbed, n):
#     length_flower = len(flowerbed)
#     last_index_check = False
#     if flowerbed[0]==1:
#         startIndex = 2
#         last_index_check = True
#     else:
#         startIndex = 3    
#     for idx in range(startIndex, length_flower, 2):
#         if n == 0:
#             return True
#         print(idx)
#         if flowerbed[idx] == 0:
#             n -= 1
#         else:
#             continue
#     if last_index_check and flowerbed[-1]==1 and n > 0:
#         return False

#     return True



# flowerbed = [1,0,0,0,0,1]
# n = 2


# print(can_place_flowers(flowerbed, n))