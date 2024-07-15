def is_subsequence(s, t):
    if len(s)==0:
        return True
    check_length = len(t)
    pointer_main = 0
    pointer_sub = 0 
    while pointer_main < check_length:
        if t[pointer_main] == s[pointer_sub]:
            pointer_main += 1
            pointer_sub += 1
            if pointer_sub == len(s):
                return True
        else:
            pointer_main += 1      
    return False


s = "abc"
t = "ahcbgdc"

print(is_subsequence(s, t))