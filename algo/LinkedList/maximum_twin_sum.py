def maximum_twin_sum(head):
    result = 0
    arr = []
    start = head
    while start!=None:
        arr.append(start.val)
        start = start.next
    i = 0
    j = len(arr)-1
    while i<j:
        sum = arr[i] + arr[j]
        if sum > result: 
            result = sum
        i += 1
        j -= 1    
    return result

class linked_list:
    def __init__(self, value):
        self.val = value
        self.next = None
node1 = linked_list(5)
node2 = linked_list(4)
node3 = linked_list(2)
node4 = linked_list(1)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next  = None


print(maximum_twin_sum(node1))