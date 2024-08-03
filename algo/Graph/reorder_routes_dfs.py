count = 0
def DFS(u, parent, adj): #recursion
    global count
    for idx, i in enumerate(adj[u]):
        v = i[0]
        if v != parent:
            check_for_actualEdge_or_imaginary = i[1]
            if check_for_actualEdge_or_imaginary:#Going away from 0
                count += 1
            DFS(v, u, adj)   


def reorder_routes(connections):
    edge_map = {}
    for i in range(len(connections)):
        u = connections[i][0]
        v = connections[i][1]
        if u not in edge_map:
            edge_map[u] = [(v, 1)]
        else:
            edge_map[u].append((v, 1))
        if v not in edge_map:    
            edge_map[v] = [(u, 0)]
        else:
            edge_map[v].append((u, 0))
    parant_of_zero = -1
    DFS(0, parant_of_zero, edge_map)
    return count

n = 6
connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]

print(reorder_routes(connections))