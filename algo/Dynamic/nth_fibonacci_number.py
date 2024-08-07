#Explaination: T0=0, T1 = 1, T2 = 1, T3 = (1+1) = 2, T4 = (1+2) = 3
#iterative way
from datetime import datetime

#iterative Constant space and o(n) time
def nth_tribinacci_num_itr(n):
    if n==0:
        return 0
    if n==1:
        return 1
    current_no = 1
    prev_no = 0
    for _ in range(2, n+1):
        next_no = current_no + prev_no
        current_no, prev_no = next_no, current_no
    return next_no    

#recursion o(2^n) exponential
def nth_tribinacci_num_rec(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return nth_tribinacci_num_rec(n-1)+nth_tribinacci_num_rec(n-2)

#memoization
def nth_tribinacci_num_rec_memo(n, DP):
    if n==0:
        return 0
    if n==1:
        return 1
    if DP[n] != -1:
        return DP[n]
    DP[n] = nth_tribinacci_num_rec_memo(n-1, DP)+nth_tribinacci_num_rec_memo(n-2, DP) 
    return DP[n]

def nth_tribinacci_num_bottom_up(n):
    dp = [-1]*(n+1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1]+dp[i-2]
    return dp[-1]    
n = 3#ans 3
print(nth_tribinacci_num_bottom_up(n))
# DP = [-1]*(n+1)
# start_time = datetime.now()
# print(f"Start time: {start_time}")
# print(nth_tribinacci_num_rec_memo(n, DP))
# start_time = datetime.now()
# print(f"Time took for iterative process is: {datetime.now()-start_time}")
# print(nth_tribinacci_num_rec(n))
# print(f"Time took for recursive process is: {datetime.now()-start_time}")
# start_time = datetime.now()
# print(nth_tribinacci_num_itr(n))
# print(f"Time took for memoization process is: {datetime.now()-start_time}")