
# Time: O(n) Space o(n)
# def findLoop(linked_list):
#     mp = {}
#     current_node = linked_list
#     while current_node.value not in mp:
#         mp[current_node.value] = 1
#         next_node = current_node.next
#         current_node = next_node   
#     return current_node.value

def findLoop(linked_list):
    first = linked_list.next
    second = linked_list.next.next
    while first != second:
        first = first.next
        second = second.next.next
    #R = D Conceptual
    first = linked_list
    while first != second:
        first = first.next
        second = second.next
    return first


class linked_list:
    def __init__(self, value):
        self.value = value
        self.next = None
node1 = linked_list(0)
node2 = linked_list(1)
node3 = linked_list(2)
node4 = linked_list(3)
node5 = linked_list(4)
node6 = linked_list(5)
node7 = linked_list(6)
node8 = linked_list(7)
node9 = linked_list(8)
node10 = linked_list(9)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = node8
node8.next = node9
node9.next = node10
node10.next = node5

res = findLoop(node1)
print(res)


