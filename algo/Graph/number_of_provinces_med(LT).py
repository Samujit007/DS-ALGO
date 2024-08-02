isConnected = [[1,1,0],
               [1,1,0],
               [0,0,1]]
n = len(isConnected)

def DFS(isConnected, u, visited):
    visited[u] = True

    for v in range(n):
        if not visited[v] and isConnected[u][v]==1:
            DFS(isConnected, v, visited)

def number_of_provinces(isConnected):
    
    visited = [False]*n
    province_count = 0
    for i in range(n):
        if not visited[i]:
            province_count += 1
            DFS(isConnected, i, visited)
    return province_count


print(number_of_provinces(isConnected))