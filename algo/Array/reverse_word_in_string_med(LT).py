def reverse_word_in_string(s):
    white_space = " "
    l, r = 0, len(s)-1
    while s[l] == white_space:
        l += 1
    while s[r] == white_space:
        r -= 1
    str_list = []

    start = l
    for idx in range(l, r):
        if s[idx] == white_space:
           str_list.append(s[start:idx])
           if s[idx-1] != white_space:
                str_list.append(s[idx]) 
           start = idx+1   
    str_list.append(s[start:r+1])
    pass
    l, r = 0, len(str_list)-1
    while l<r:
        str_list[l], str_list[r] = str_list[r], str_list[l]
        l += 1
        r -= 1
    return "".join(str_list)    




s = "the sky is blue"
print(reverse_word_in_string(s))