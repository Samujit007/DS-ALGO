#Time: O(nlogn), Space: O(1)
def nonConstructibleChange(coins):
    # Write your code here.
    if len(coins) == 0:
        return 1
    coins = sorted(coins) #Time: O(nlogn)
    if coins[0] > 1:
        return 1
    first_coin = coins[0]
    change = first_coin
    for idx, val in enumerate(coins):
        if idx!=0:
            next_coin = val
            if next_coin <= change + 1:
                change += next_coin
            else:
                return change +1	
    return change+1


a = [5, 7, 1, 1, 2, 3, 22]
print(nonConstructibleChange(a))