def keys_and_rooms(rooms):
    visited = [False]*len(rooms)
    find_room_open_chances(rooms, 0, visited)
    for i in visited:
        if i == False:
            return False
    return True

def find_room_open_chances(rooms, source, visited):
    visited[source] = True
    for key in rooms[source]:
        if not visited[key]:
            find_room_open_chances(rooms,key, visited)




rooms = [[1,3],[3,0,1],[2],[0]]#[[1],[2],[3],[]]

print(keys_and_rooms(rooms))