def delete_middle_node_of_linked_List_med(head):
    if head.next==None:
            return
    length = 0
    current = head
    while current != None:
        length += 1
        current = current.next
    mid_elm = length//2    
    current = head
    counter = 0
    prev = head
    while current is not None and counter < mid_elm:
        prev = current
        current = current.next
        counter += 1
    prev.next = current.next
    return head

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
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = None

res = delete_middle_node_of_linked_List_med(node1)
print(res)