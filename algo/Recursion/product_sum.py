#Brute Force

def productSum(arr):
    ans = 0
    for idx, i in enumerate(arr):
        res = 0
        if isinstance(i, list):   
            res = 2*(calc(res, i))
        else:
            res = i    
        ans += res
        pass
    return ans

def calc(res, gran_arr, level=2):
    if len(gran_arr) == 0:
        return res 
    each_elem = gran_arr.pop(0)
    if isinstance(each_elem, list):
        product = (level+1)*(calc(0, each_elem, level+1))
        a_sum = calc(res, gran_arr, level)
        return product + a_sum
    else:
        res += each_elem
        return calc(res, gran_arr, level)
           
    # temp_res = 0
    # for i in gran_arr:
    #     if isinstance(i, list):
    #         return res + calc(res, i, level+1)
    #     else:
    #         temp_res += i
    # res = temp_res      
    # return 2* res


arr = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
print(productSum(arr))