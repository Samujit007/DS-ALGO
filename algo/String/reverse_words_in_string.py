#My approach
#Time: O(n) | Space: O(n)
# def rev_string(input_str):
#     list_str = list(input_str)
#     list_words = []
#     word_finder = []
#     space_finder = []
   
#     for i,j in enumerate(list_str):  
#         if j == " ":
#             space_finder.append(j)
#             if i != len(list_str)-1:
#                 if list_str[i+1] !=" ":
#                     list_words.append("".join(space_finder)) 
#                     space_finder = []
#             else:
#                 list_words.append("".join(space_finder)) 
#                 space_finder = []    
#         else:
#             word_finder.append(j)
#             if i != len(list_str)-1:
#                 if list_str[i+1] ==" ":
#                     list_words.append("".join(word_finder))
#                     word_finder = []
#             else:
#                 list_words.append("".join(word_finder))
#                 word_finder = []  
#     out = []
#     for i in list_words[::-1]:
#         # print(i)
#         out.append(i)
#     return "".join(out)    
# input_str = "this  is best! "
# print(rev_string(input_str))
#================================================================== Split and reverse
#Time: O(n) | Space: O(n)
def rev_string(input_str):
    list_words = []
    counter = 0 
    for i in range(len(input_str)):  
        char = input_str[i]
        if char == " ":
            list_words.append(input_str[counter:i])
            counter = i
        elif input_str[counter] == " ":
            list_words.append(" ")
            counter = i
    list_words.append(input_str[counter:])
    print(list_words)
    reverseList(list_words)
    return "".join(list_words)

def reverseList(list_words):
    start , end = 0, len(list_words)-1
    while start < end:
        list_words[start], list_words[end] = list_words[end], list_words[start]
        start += 1
        end -= 1
input_str = "this  is best!"
print(rev_string(input_str))