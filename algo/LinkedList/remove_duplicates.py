def removeDuplicates(linked_list):
    
    current_node = linked_list
    while current_node !=None:
        next_node = current_node.next
        while next_node is not None and next_node.value == current_node.value:
            next_node = next_node.next
        
        current_node.next = next_node
        current_node = next_node
        pass
    print(linked_list)        
class linked_list:
    def __init__(self, value):
        self.value = value
        self.next = None
node1 = linked_list(1)
node2 = linked_list(1)
node3 = linked_list(3)
node4 = linked_list(4)
node5 = linked_list(4)
node6 = linked_list(4)
node7 = linked_list(5)
node8 = linked_list(6)
node9 = linked_list(6)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = node8
node8.next = node9
node9.next = None
print(removeDuplicates(node1))


