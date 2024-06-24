def reverseLinkedList(linked_list):
    #In: 0 -> 1 -> 2 -> 3 -> 4 -> 5
    #Out: 5 -> 4 -> 3 -> 2 -> 1 -> 0

    p1 = None
    p2 = linked_list

    while p2 != None:
        p3 = p2.next
        p2.next = p1
        p1 = p2
        p2 = p3
    return p1


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

res = reverseLinkedList(node1)
print(res)


