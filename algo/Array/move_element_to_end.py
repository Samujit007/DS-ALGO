def moveElementToEnd(arr, to_move):
    first_pointer = 0
    last_pointer = len(arr) - 1
    while first_pointer < last_pointer:
        while first_pointer != len(arr)-1 and arr[first_pointer] != to_move:
           first_pointer += 1

        while last_pointer != 0 and arr[last_pointer] == to_move:
            last_pointer -= 1
        if first_pointer > last_pointer:
            break
        arr[first_pointer], arr[last_pointer] = arr[last_pointer], arr[first_pointer]
    return arr


arr = [2, 1, 2, 2, 2, 3, 4, 2]#[3, 3, 3, 3, 3]#[1, 2, 4, 5, 6]#[2, 4, 2, 5, 6, 2, 2]#[2, 1, 2, 2, 2, 3, 4, 2]
to_move = 2

print(moveElementToEnd(arr, to_move))

