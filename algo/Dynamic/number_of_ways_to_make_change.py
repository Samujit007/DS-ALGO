#Time o(n*t) |Space o(t)
def minCoins(arr, target):
    target_arr = [1 if amount==0 else 0 for amount in range(target+1)]
    for denom in arr:
        for amount,val in enumerate(target_arr):
            if target==0:
                return target_arr[0]
            if amount==0:
                pass     
            elif denom <= amount:
                left_amount = amount-denom
                target_arr[amount] = target_arr[amount] + target_arr[left_amount]#min(target_arr[amount],1+target_arr[left_amount])
    print(target_arr)
    return target_arr[-1] if target_arr[-1] != 0 else 0

arr = [1, 5]#, 10, 25]#[1, 5, 10, 25]#[5]#[1, 5]#[2, 3, 4, 7]
target = 10#9#6#0
print(minCoins(arr, target))