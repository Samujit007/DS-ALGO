#Time o(n) space o(n)
def runLengthEncoding(str_in):
    if len(str_in) == 1:
        return str(1)+str_in[0]
    out = []
    counter = 1
    for idx in range(len(str_in)):
        if idx != len(str_in)-1:
            if str_in[idx] == str_in[idx+1]:       
                if counter==9:
                    out.append("".join([str(counter),str_in[idx+1]]))  
                    counter = 0 
                counter +=1 
                if idx+1 == len(str_in)-1:
                    out.append("".join([str(counter),str_in[idx+1]]))  
            else:
                out.append("".join([str(counter),str_in[idx]]))   
                counter = 1
                if idx+1 == len(str_in)-1:
                    out.append("".join([str(counter),str_in[idx+1]])) 
        pass
    return "".join(out)    


str_in = "AAAAAAAAAAAAABBCCCCDD"
#"AAAAAAAAAAAAABBCCCCDD"#"AABCCCD"

print(runLengthEncoding(str_in))