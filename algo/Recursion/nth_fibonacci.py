# def nthFibonacci(num, out):
#     if num==0:
#         return out
#     else:
#         if len(out)==0:
#             out.append(0)
#             if num <= 1:
#                 return out 
#             out.append(1)
#             if num <= 2:
#                 return out
#             num -= 2 
#             return nthFibonacci(num, out)   
#         else:
#             last_elem = out[-1] 
#             second_last = out[-2]
#             out.append(last_elem+second_last)
#             return nthFibonacci(num-1, out)


# num = 6
# out = []
# print(nthFibonacci(num, out))

def nthFibonacci(n, map = {}):
    if n in map:
        return map[n]
    if n <= 2:
        return 1
    s1 = nthFibonacci(n-1) 
    s2 = nthFibonacci(n-2)
    map[n] = s1+s2
    return map[n]   

n = 6
print(nthFibonacci(n))


