#Time O(nlogn) space o(1)

def classPhotos(red, blue):
    det_first_row_color = 'red' if red[0] < blue[0] else 'blue' 
    red = sorted(red)
    blue = sorted(blue)
    for idx in range(0, len(red)):
        if det_first_row_color =='red':
            if red[idx] >= blue[idx]:
                return False
        if det_first_row_color =='blue':
            if red[idx] <= blue[idx]:
                return False
    return True

red = [2, 4, 7, 5, 1]#[6]#[5, 8, 1, 3, 4]
blue = [3, 5, 6, 8, 2]#[6]#[6, 9, 2, 4, 5]
print(classPhotos(red, blue))