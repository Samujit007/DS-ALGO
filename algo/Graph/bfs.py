def dfs(graph, array):
    q = []
    q.append(graph)
    while q != []:
        current_node = q.pop(0)
        array.append(current_node.name)
        for ch in current_node.children:
            q.append(ch)
        
    return array

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name
    
    def addChild(self, name):
        self.children.append(Node(name))
        return self

graph = Node("A")
graph.addChild("B").addChild("C").addChild("D") 
graph.children[0].addChild("E").addChild("F")
graph.children[2].addChild("G").addChild("H")
graph.children[0].children[1].addChild("I").addChild("J")
graph.children[2].children[0].addChild("K")
print(dfs(graph, []))

