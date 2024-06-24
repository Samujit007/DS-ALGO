
def validIP(str_in):
    upper_bound = 255
    out = []
    first_sec, second_sec, third_sec = 0 
    # for idx in range(len(str_in)):

     
    while str_in[first_sec] <= upper_bound or str_in[second_sec] <= upper_bound or str_in[third_sec] <= upper_bound:
        first_d = str_in[:first_sec]
        second_d = str_in[:second_sec]
        third_d = str_in[:second_sec]
        if first_d <= upper_bound:
            second_d
        pass
    
    
    pass
    
ip_add = "1921680"

print(validIP(ip_add))
