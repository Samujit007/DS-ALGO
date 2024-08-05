pick = 6
def guess(num):
    return 0 if  num == pick else -1 if num > pick else num < pick 

def guess_number_higher_or_lower_easy(n, pick):
    l = 1
    r = n
    while l <= r:
        m = l + (r-l)//2
        res = guess(m)
        if res==0:
            return m
        if res > 0:
            l = m+1
        elif res < 0:
            r = m - 1
    return -1           

n = 10
pick = 6

print(guess_number_higher_or_lower_easy(n, pick))