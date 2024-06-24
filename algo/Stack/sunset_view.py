def sunsetView(arr, dir):
    out = []
    top_Building = 0
    for idx, i in enumerate(arr):
        if dir == "East":
            if arr[idx] > top_Building:
                top_Building = arr[idx]
            if arr[idx] <= top_Building:
                if idx==0:
                    out.append(idx)
                else:
                    last_lowest = out[-1]
                    if arr[idx] < arr[last_lowest]:
                            out.append(idx)
                    else:
                        while arr[idx] >= arr[last_lowest]:        
                            out.pop()
                            if len(out) ==0 :
                                break 
                            last_lowest = out[-1]
                        out.append(idx) 
        else:
            if idx == 0:
                out.append(idx)
            else:
                last_heighest = out[-1]
                if arr[idx] > arr[last_heighest]:
                    out.append(idx)
                pass                
    return out

arr = [1, 2, 3, 4, 5, 6]#[3, 5, 4, 4, 3, 1, 3, 2]
dir = "West"

print(sunsetView(arr, dir))