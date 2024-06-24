def longestSubstringWithoutDuplication(str_in):
    st_out = ""
    st_long = ""
    for idx in range(len(str_in)):
        if str_in[idx] not in st_out:
            st_out += str_in[idx]
        else:
            if len(st_out) > len(st_long):
                st_long = st_out
            st_out = "" 
            left_idx = idx-1
            while str_in[left_idx] != str_in[idx]:
                st_out = str_in[left_idx] + st_out
                left_idx -=1
            st_out += str_in[idx]
        pass
    return st_out if len(st_out) > len(st_long) else st_long if st_long != "" else st_out
        
str_in = "abcb"
#"abcdabcef"#"clementisanarm"#"abccdeaabbcddef"#"a"#"clementisacap"
print(longestSubstringWithoutDuplication(str_in))  