def groupAnagrams(str_in):
    str_map = {}
    out = []
    for idx, i in enumerate(str_in):
        i_sort = "".join(sorted(i))
        if i_sort not in str_map:
            str_map[i_sort] = [i]
        else:
            str_map[i_sort].append(i)   
        pass
    pass
    for i in str_map.values():
        out.append(i)
    return out
    
str_1 = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]
print(groupAnagrams(str_1))