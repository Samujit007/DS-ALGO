def firstNonRepeatingChar(str_in):
    store = {}
    res = ""
    for i in range(len(str_in)):
        if str_in[i] not in store:
            store[str_in[i]] = 1
        else:
            store[str_in[i]] +=1 
    for key in store.keys():
        if store[key]==1:
            res = key
            break
    return -1 if res == "" else str_in.find(res)    
    
        
str_in = "ababaccd"#"abcdcaf"
print(firstNonRepeatingChar(str_in))  