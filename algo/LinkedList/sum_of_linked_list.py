from typing import Counter


def sumOfLinkedList(linked_list_1, linked_list_2):
    first_arr = []
    second_arr = []
    current_node = linked_list_1
    while current_node != None:
        first_arr.insert(0,current_node.value)
        current_node = current_node.next
    current_node = linked_list_2    
    while current_node != None:
        second_arr.insert(0,current_node.value)
        current_node = current_node.next
    sum = str(int("".join(map(str, first_arr))) + int("".join(map(str, second_arr))))[::-1]
    out_Linked_list = linked_list(int(sum[0]))
    counter = 1
    head = out_Linked_list
    while counter < int(len(str(sum))):
        new_node = linked_list(int(sum[counter]))
        out_Linked_list.next = new_node
        out_Linked_list = out_Linked_list.next
        counter += 1 
    return head



class linked_list:
    def __init__(self, value):
        self.value = value
        self.next = None
node11 = linked_list(2)
node12 = linked_list(4)
node13 = linked_list(7)
node14 = linked_list(1)
node11.next = node12
node12.next = node13
node13.next = node14
node14.next = None
node21 = linked_list(9)
node22 = linked_list(4)
node23 = linked_list(5)
node21.next = node22
node22.next = node23
node23.next = None

res = sumOfLinkedList(node11, node21)
print(res)


