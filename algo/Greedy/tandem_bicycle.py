#Time O(nlogn) space o(1)

from pickle import FALSE


def tandemBicycle(red, blue, fastest):
    red = sorted(red)
    blue = sorted(blue) if fastest else sorted(blue)[::-1]
    speed = 0
    for rdx in range(0, len(red)):
        bdx = len(blue)-rdx-1
        max_speed = max(red[rdx], blue[bdx])
        speed += max_speed
    
    return speed   

red = [5, 5, 3, 9, 2]
blue = [3, 6, 7, 2, 1]
fastest = False
print(tandemBicycle(red, blue, fastest))