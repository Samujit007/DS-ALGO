def levenshteinDistance(str1, str2):
    twoD_arr = [[i for i in range(len(str1)+1)] for j in range(len(str2)+1)]
    for i in range(1, len(str2)+1):
        twoD_arr[i][0] = twoD_arr[i-1][0]+1
    for idx in range(1, len(str2)+1):
        for jdx in range(1, len(str1)+1):
            if str2[idx-1]==str1[jdx-1]:
                twoD_arr[idx][jdx] = twoD_arr[idx-1][jdx-1] # diagonal
            else:
                twoD_arr[idx][jdx] = 1 + min(twoD_arr[idx-1][jdx-1], twoD_arr[idx][jdx-1], twoD_arr[idx-1][jdx])
    
    return twoD_arr[len(twoD_arr)-1][len(twoD_arr[len(twoD_arr)-1])-1]

str1 = "abc"
str2 = "yabd"

print(levenshteinDistance(str1, str2))
