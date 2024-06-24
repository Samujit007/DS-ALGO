# def removeKthElementFromEnd(linked_list, k):
#     current_node = linked_list
#     first_var = 0
#     second_var = 0
#     while current_node !=None:
#         next_node = current_node.next
#         current_node = next_node
#         if second_var<k:
#             second_var += 1
#         else:
#             first_var += 1
#             second_var += 1 
#     idx = 0
#     current_node = linked_list
#     next_node = current_node.next
#     while idx < first_var-1:
#         current_node.next = next_node
#         current_node = next_node
#         next_node = current_node.next
#         idx +=1
#     if first_var == 0:
#         return next_node
#     else:    
#         next_node = next_node.next
#         current_node.next = next_node
#     return linked_list

#o(n) | o(1) 
def removeKthElementFromEnd(linked_list, k):
    counter = 0
    first_var = linked_list
    second_var = linked_list
    while counter <= k:
        second_var = second_var.next
        counter += 1
    if second_var is None:
        linked_list.value = linked_list.next.value  
        linked_list.next = linked_list.next.next
        return

    while second_var is not None:
        second_var = second_var.next
        first_var = first_var.next
    first_var.next = first_var.next.next

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
node10.next = None
k = 4
res = removeKthElementFromEnd(node1, k)
print(res)


