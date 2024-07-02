def greatest_comn_div_of_strings(str1,str2):  
    s1 = max(str1, str2, key = lambda x: len(x))
    if s1 == str1:
        s2 = str2
    else:
        s2 = str1
    a1, a2 = len(s1), len(s2)

    if s2 * (a1//a2) == s1:
        return s2
    
    for i in range(2, a2//2 + 1):
        if (a2 / i) % 1 == 0:
            if s2[:a2//i]*i == s2:
                if s1[:a2//i]*int(i*a1/a2) == s1:
                    if s2[:a2//i] == s1[:a2//i]:
                        return s2[:a2//i] 

    if s1.count(s1[0]) == a1:
        if s2.count(s2[0]) == a2:
            if s1[0] == s2[0]:
                return s1[0]

    return ''

str1 =  "ABABAB"#"ABCABC"#"LEET"#"ABCDEF" #"ABABABAB"#"LEET"#"ABCABC" # "ABABABAB" # "LEET"
str2 =  "ABAB"#"CODE"#"ABC"    #"ABAB"#"CODE"#"ABC"    # "ABAB" # "CODE"

print(greatest_comn_div_of_strings(str1,str2))

# def greatest_comn_div_of_strings(str1,str2):
#     if str1[0] != str2[0]:
#         return ""
#     n = len(str1)
#     m = len(str2)
#     final_out = ""
#     temp_str = ""
#     for idx in range(max(n, m)):
#         if idx < min(n, m):
#             if str1[idx] == str2[idx]:
#                 if str1[idx] not in temp_str:
#                     temp_str += str1[idx]
#                 else:
#                     final_out = temp_str
#                     temp_str = ""
#                     temp_str += str1[idx]
#         else:
#             if temp_str==final_out:
#                 return final_out 
#             final_out += str1[idx]

                
#     return final_out if final_out==temp_str else ""

# str1 =  "ABABABAB"#"ABCABC"#"LEET"#"ABCDEF" #"ABABABAB"#"LEET"#"ABCABC" # "ABABABAB" # "LEET"
# str2 =  "ABAB"#"CODE"#"ABC"    #"ABAB"#"CODE"#"ABC"    # "ABAB" # "CODE"

# print(greatest_comn_div_of_strings(str1,str2))