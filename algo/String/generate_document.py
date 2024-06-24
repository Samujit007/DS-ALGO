#Time o(n) space o(n)
def generate_document(str_char, str_doc):
    str_chr_map = {}

    for idx in range(len(str_doc)):
        if str_doc[idx] in str_char:
            if str_doc[idx] in str_chr_map:
                if str_char.count(str_doc[idx]) > str_chr_map[str_doc[idx]]:
                    str_chr_map[str_doc[idx]] += 1
                else:
                    return False    
            else:
                str_chr_map[str_doc[idx]] = 1        
        else:
            return False    
        pass
    return True    


chars = "Bste!hetsi ogEAxpelrt x "#"aheaolabbhb"
doc = "AlgoExpert is the Best!"#"hello"#
print(generate_document(chars, doc))