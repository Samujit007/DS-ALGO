#time o(n) space o(n)

def merge_str_alt(word1, word2):
    n = len(word1)#o(1)
    m = len(word2)#o(1)
    merged = ""
    for i in range(max(n,m)):#o(1)
        if i<n and i<m:
            merged += word1[i] + word2[i]
        elif i>=n:
            merged += word2[i]    
        else:
            merged += word1[i]    
    return merged


word1 = "ab" 
word2 = "pqrs"

print(merge_str_alt(word1, word2))