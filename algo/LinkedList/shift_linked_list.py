def shiftLinkedList(head, k):
    listLength = 1
    listTail = head
    while listTail is not None:
        listTail = listTail.next
        listLength += 1



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
k = 4
res = shiftLinkedList(node1, k)
print(res)