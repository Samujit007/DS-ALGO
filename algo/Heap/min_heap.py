class minHeap:
    def __init__(self, array) -> None:
        self.heap = self.buildHeap(array)
    
    def buildHeap(self,array):

    def siftDown(self,currentIndex, endIndex, heap):

    def siftUp(self,currentIndex, heap):

    def peek(self):
        return self.heap[0]

    def remove(self):
        
    def insert(self, value):
        self.heap.append(value)
        self.siftUp(len(heap)-1, self.heap)

    def swap(self, i, j, heap):
       heap[i], heap[j] = heap[j], heap[i] 