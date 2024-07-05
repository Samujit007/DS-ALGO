def reverse_vowels(s):
    # vowel_map={
    #     'A':True,
    #     'E':True,
    #     'I':True,
    #     'O':True,
    #     'U':True,
    #     'a':True,
    #     'e':True,
    #     'i':True,
    #     'o':True,
    #     'u':True
    # }
    vowel_map_str = "aeiouAEIOU"
    first = 0
    s = list(s)
    last = len(s)-1
    while first<last:
        if s[first] in vowel_map_str and s[last] in vowel_map_str: 
            s[first], s[last] = s[last], s[first]
            first +=1
            last-=1
        elif s[first] not in vowel_map_str:
            first += 1
        else:
            last -= 1        
    return "".join(s)

s = "aA"
#"holle"
print(reverse_vowels(s))