#My approach
# def isPalindrome(str_in):
#     str_out = str_in[::-1] #reverse string or reverse loop
#     return str_in == str_out

# str_in = "abcdcba"
# print(isPalindrome(str_in))   

 
#===================================================================================
#Time: O(n*2) | Space: O(n) as appneding to a string is not a constant time operation, it has to iterate through all the existing chars in a string 

# def isPalindrome(str_in):
#     rev_str = ""
#     for i in reversed(range(len(str_in))):
#         rev_str += str_in[i]
#     return str_in == rev_str

# str_in = "abcdcba"
# print(isPalindrome(str_in))   

#==================================================================================================  
#Time: O(n) | Space: O(n) as appneding to a list is a constant time operation

# def isPalindrome(str_in):
#     rev_str = []
#     for i in reversed(range(len(str_in))):
#         rev_str.append(str_in[i])
#     return str_in == "".join(rev_str)

# str_in = "abcdcba"
# print(isPalindrome(str_in))    

#==================================Recursion=================================================================
#Time: O(n) | Space: O(n) because of call stack
# def isPalindrome(str_in):
#     if len(str_in) > 0:
#         first = str_in[0]
#         last = str_in[-1] #last index
#         middle = str_in[1:-1]   
#         if first == last:
#              return isPalindrome(middle)  
#         else:
#             return False     
#     else:
#         return True              
       

# str_in = "aabcdcbaa"
# print(isPalindrome(str_in))  
#===========================Pointer===================

#Time: O(n) | Space: O(1) Best algo among others
def isPalindrome(str_in):
    first_index =  0            
    last_index = len(str_in)-1
    while first_index < last_index: 
        if str_in[first_index] != str_in[last_index]:
            return False
        else:    
            first_index += 1
            last_index -= 1
    return True    
str_in = "abcba"
print(isPalindrome(str_in))  