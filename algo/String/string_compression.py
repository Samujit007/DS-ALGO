# String Compression

# Given an array of characters chars, compress it using the following algorithm:

# Begin with an empty string s. For each group of consecutive repeating characters in chars:

# If the group's length is 1, append the character to s.
# Otherwise, append the character followed by the group's length.
# The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

# After you are done modifying the input array, return the new length of the array.

# You must write an algorithm that uses only constant extra space.

 

# Example 1:

# Input: chars = ["a","a","b","b","c","c","c"]
# Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
# Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
# Example 2:

# Input: chars = ["a"]
# Output: Return 1, and the first character of the input array should be: ["a"]
# Explanation: The only group is "a", which remains uncompressed since it's a single character.
# Example 3:

# Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
# Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
# Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".

# def string_compression(chars):
#     #base case
#     if len(chars) == 1:
#         return len(chars[0])
#     out = chars[0]
#     counter = 1
#     for idx in range(1, len(chars)):
#         if chars[idx] == chars[idx-1]:
#             counter += 1
#         else:
#             if counter!=1:
#                 out = out+str(counter)
#             counter = 1#reset the counter
#             out = out + chars[idx]
#     if counter > 1:
#         out = out+str(counter)
#     chars = list(out)    
#     return len(out)

# chars = ["a","a","b","b","c","c","c"]#["a","b","b","b","b","b","b","b","b","b","b","b","b"]
# #["a"]#["a","a","b","b","c","c","c"]

# print(string_compression(chars))
def split_longer_numbers(val):# recursion will return concatinated string
    if val < 10:
        return str(val)
    else:
        return split_longer_numbers(val // 10) + "', '" + str(val % 10)

def string_compression(chars):
    #base case
    if len(chars) == 1:
        return len(chars[0])
    counter = 1
    idx = 1
    letter_start_pos = 1
    while idx <= len(chars)-1:
        if chars[idx] == chars[idx-1]:
            counter += 1
            idx += 1
        else:
            if counter!=1:
                chars[letter_start_pos] = split_longer_numbers(counter)
                letter_start_pos += 2 + len(str(counter))-1
            else:
                letter_start_pos += 1
            counter = 1#reset the counter
            idx += 1
                
    if counter > 1:
        # if 
        chars[letter_start_pos] = str(counter)
        chars = chars[:letter_start_pos+1]
    # chars = list(out)    
    return len(chars)

chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b", "c"]
#["a"]#["a","a","b","b","c","c","c"]
# t = split_longer_numbers(101)
print(string_compression(chars))