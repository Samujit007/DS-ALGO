def split_longer_numbers(val):# recursion
    if val < 10:
        return [val]
    else:
        return split_longer_numbers(val // 10) + [val % 10]


def string_compression(chars):
    if len(chars)==1:
        return len(chars)
    
    count = 1
    idx = 1
    char_idx = 0
    current_char = chars[0]
    while idx < len(chars):
        if chars[idx] == current_char:
            count += 1
        else:
            chars[char_idx] = current_char
            char_idx += 1
            chars[char_idx] = str(count)
            char_idx += 1
            current_char = chars[idx]
            count = 1
        idx += 1
        if idx == len(chars):
            chars[char_idx] = current_char
            char_idx += 1
            chars[char_idx] = str(count)
    chars = chars[:char_idx+1]
    return len(chars)

chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
print(string_compression(chars))

#Did not pass all the test cases
# def split_longer_numbers(val):# recursion
#     if val < 10:
#         return [val]
#     else:
#         return split_longer_numbers(val // 10) + [val % 10]

# def string_compression(chars):
#     if len(chars)==1:
#         return len(chars)
    
#     count = 1
#     idx = 1
#     char_idx = 1
#     while idx < len(chars):
#         if chars[idx] == chars[idx-1]:
#             count += 1
#         else:
#             if count!=1:
#                 if count > 9:
#                     res = [str(element) for element in split_longer_numbers(count)]
#                     for i in res:
#                         chars[char_idx] = str(i)
#                         char_idx += 1
#                 else:
#                     chars[char_idx] = str(count)    
#                 char_idx += 2    
#             else:        
#                 char_idx += 1
#             count = 1 
#         idx += 1
#         if idx == len(chars):
#             if count!=1:
#                 if count > 9:
#                     res = [str(element) for element in split_longer_numbers(count)]
#                     for i in res:
#                         chars[char_idx] = str(i)
#                         char_idx += 1
#                     char_idx-=1
#                 else:
#                     chars[char_idx] = str(count)                 
#     chars = chars[:char_idx+1]
#     return len(chars)

# chars = ["a","a","a","b","b","a","a"] 
# #["a","a","b","b","c","c","c"]
# # ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
# print(string_compression(chars))
# # print(split_longer_numbers(113123214324254))