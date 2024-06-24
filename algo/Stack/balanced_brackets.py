def isValid(str_in):
    map = {"]":"[", "}":"{", ")":"("}
    opens = "({["
    closes = ")}]"
    # bracks = "({[)}]" 
    stack = []
    for i in range(len((str_in))):
        if str_in[i] in opens or str_in[i] in closes:
            if str_in[i] not in map.keys():
                stack.append(str_in[i])  
            else:
                if len(stack) != 0 and stack[-1] == map[str_in[i]]:
                    stack.pop()
                else: 
                    return False      
    return True if len(stack) == 0 else False    
str_in = "{[[[[({)]]]]}"#"({)"#"([[{}]])"#"{[[[[({})]]]]}"

print(isValid(str_in))