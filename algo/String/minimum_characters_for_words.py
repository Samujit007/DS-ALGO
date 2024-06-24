def minimumCharactersForWords(str_in):
    mn_map = {}
    out = []
    for idx, i in  enumerate(str_in):
        chr_Map = {}
        for cdx in range(len(i)):
            if i[cdx] not in chr_Map:
                chr_Map[i[cdx]] = 1
            else:
                chr_Map[i[cdx]] += 1   
        for k,v in chr_Map.items():
            if k not in mn_map:
                mn_map[k] = v
            else:
                if v > mn_map[k]: 
                    mn_map[k] = v 
                pass
            pass
    for key, val in mn_map.items():
        for j in range(val):
            out.append(key)
    return out
    
        
str_in = ["this", "that", "did", "deed", "them!", "a"]
print(minimumCharactersForWords(str_in))  