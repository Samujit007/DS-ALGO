def odd_even_linked_list(head):
    if head is None or head.next is None:
        return head
    odd_node = head
    even_node = head.next
    even_start = even_node# for connecting 
    while even_node and even_node.next:
        temp_next_odd = even_node.next
        odd_node.next = even_node.next
        even_node.next = even_node.next.next
        odd_node = odd_node.next
        even_node = even_node.next
    odd_node.next = even_start
    return head


    pass

class linked_list:
    def __init__(self, value):
        self.value = value
        self.next = None
node1 = linked_list(1)
node2 = linked_list(2)
node3 = linked_list(3)
node4 = linked_list(4)
node5 = linked_list(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = None



res = odd_even_linked_list(node1)
