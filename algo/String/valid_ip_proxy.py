#o(1) o(1)

def validIP(string):
    ipAddFound = []

    for i in range(1, min(len(string), 4)):
        currentIPAdd = ['', '', '', '']

        currentIPAdd[0] = string[:i]
        if not isValidPart(currentIPAdd[0]):
            continue
        for j in range(i+1, i + min(len(string)-i, 4)):
            currentIPAdd[1] = string[i:j]
            if not isValidPart(currentIPAdd[1]):
                continue
            for k in range(j+1, j + min(len(string)-j, 4)):      
                currentIPAdd[2] = string[j:k]
                currentIPAdd[3] = string[k:]

                if isValidPart(currentIPAdd[2]) and isValidPart(currentIPAdd[3]):
                    ipAddFound.append('.'.join(currentIPAdd))
    return ipAddFound

def isValidPart(string):
    stringAsInt = int(string)
    if stringAsInt > 255:
        return False
    return len(string) == len(str(stringAsInt))    

st = "1921680"
print(validIP(st))