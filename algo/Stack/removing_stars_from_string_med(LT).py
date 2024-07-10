def removing_stars_from_string_med(s):
    stck = []
    star = "*"
    for i in s:
        if i != star:
            stck.append(i)
        else:
            stck.pop()    
    return "".join(stck)


s = "leet**cod*e"
#"lecoe"   

print(removing_stars_from_string_med(s))