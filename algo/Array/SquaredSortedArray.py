#Not optimal
#Time O(n*nlogn),Space o(n) 
# def sortedSquaredArray(array):
#     out = []
#     for i in array:
#         out.append(i*i)
#     return sorted(out)

# a = [-2, 1, 3, 6, 9]
# print(sortedSquaredArray(a))
    
#===Time: O(n) , SPace O(n)
def sortedSquaredArray(array):
    # Write your code here.
    out = []
    smallest = 0 
    largest = len(array) - 1
    for i in range(len(array)):
        if abs(array[smallest]) >  abs(array[largest]):
            out.insert(0,array[smallest]*array[smallest])
            smallest = smallest+1
        else:
            out.insert(0,array[largest]*array[largest])
            largest = largest-1	
    return out
   

a = [-3,1,2]
print(sortedSquaredArray(a))