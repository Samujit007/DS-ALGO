#Time o(n*t) |Space o(t)
def minCoins(arr, target):
    target_arr = [float('inf') for amount in range(target+1)]
    for denom in arr:
        for amount,val in enumerate(target_arr):
            if amount==0:
                target_arr[amount] = 0
            elif denom <= amount:
                left_amount = amount-denom
                target_arr[amount] = min(target_arr[amount],1+target_arr[left_amount])
    print(target_arr)
    return target_arr[target] if target_arr[target] != float("inf") else -1

arr = [1, 2, 3,4,8,9]
target = 7
print(minCoins(arr, target))