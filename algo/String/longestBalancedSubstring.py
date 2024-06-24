def longestBalancedSubstring(strr):
    maxLength = 0
    indexStack = []
    indexStack.append(-1)

    for i in range(len(strr)):
        if strr[i] == "(":
            indexStack.append(1)
        else:
            indexStack.pop()  
            if len(indexStack) ==0 :
                indexStack.append(1)
            else:
                balancedSubStringIdx = indexStack[len(indexStack)-1]
                currentLength = i - balancedSubStringIdx
                maxLength = max(maxLength, currentLength)
    return maxLength

strr = "(()))("

print(longestBalancedSubstring(strr))