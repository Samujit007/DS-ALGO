def generateDivTags(number):
    matchedDivTags = []
    generateDivTagsFromPrefix(number, number, '', matchedDivTags)
    return matchedDivTags

def generateDivTagsFromPrefix(openTagNeeded, closeTagNeeded, prefix, result):
    if openTagNeeded > 0:
        newPrefix = prefix + "<div>"
        generateDivTagsFromPrefix(openTagNeeded-1, closeTagNeeded, newPrefix, result)
    if openTagNeeded < closeTagNeeded:
        newPrefix = prefix + "</div>"
        generateDivTagsFromPrefix(openTagNeeded, closeTagNeeded-1, newPrefix, result)    
    if closeTagNeeded == 0 :
        result.append(prefix)

number = 3
print(generateDivTags(number))