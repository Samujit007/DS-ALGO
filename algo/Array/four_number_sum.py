def fourNumberSum(arr, target_sum):
    h_map = {}
    quad = []
    for idx in range(1, len(arr)):
        for aft in range(idx+1, len(arr)):
            sum = arr[idx] + arr[aft]
            diff = target_sum - sum
            if diff in h_map:
                
                diff_pair = h_map[diff]
                for i in diff_pair:
                    elem = []
                    for j in i:
                        elem.append(j)
                    elem.append(arr[idx])
                    elem.append(arr[aft]) 
                    quad.append(elem)        
        for prev in range(0, idx):
            sum = arr[idx] + arr[prev]
            predicted_rem = target_sum - sum
            if sum not in h_map:
                h_map[sum] = [[arr[prev], arr[idx]]]
            else:
                h_map[sum].append([arr[idx], arr[prev]])    
    return quad

arr = [5, -5, -2, 2, 3, -3]#[7, 6, 4, -1, 1, 2]
target_sum = 0#16
print(fourNumberSum(arr, target_sum))