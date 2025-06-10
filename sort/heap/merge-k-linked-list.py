import math
class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class PriorityQueue:

    def __init__(self):
        self.heap = []


    def comparation (self,n1:Node,n2:Node):
        return n1.val - n2.val

    def enqueue(self,node):
        self.heap.append(node)
        self.bubbleUpSort()

    def bubbleUpSort(self):
        index = len(self.heap) - 1
        

        while index > 0:
            element = self.heap[index]
            parentIndex = math.floor((index -1)/2)
            parent = self.heap[parentIndex]

            if (self.comparation(element,parent) < 0): break

            self.heap[parentIndex] = element
            self.heap[index] = parent
            index = parentIndex

    def dequeue(self):
        max = self.heap[0]
        end = self.heap.pop()

        if (len(self.heap) > 0):
            self.heap[0] = end
            self.sinkDownComparation(0)
        return max
    
    def sinkDownComparation(self,index):
        left,right,parent = (index*2)+1,(index*2)+2,index
        length = len(self.heap)
        if left < length and self.comparation(self.heap[left], self.heap[parent])>0:
            parent = left

        if right < length and self.comparation(self.heap[right], self.heap[parent])>0:
            parent = right

        if parent != index :
            [self.heap[parent],self.heap[index]] = [
                self.heap[index],self.heap[parent]
            ]
            self.sinkDownComparation(parent)
        
    def isEmpty(self): return len(self.heap) == 0

def MergeKList(list):

    pq = PriorityQueue()

    for nest in list:
        if nest != None: pq.enqueue(nest)

    dummy = Node(-1)
    last = dummy

    while not pq.isEmpty() :
        top = pq.dequeue()
        last.next = top
        last = top

        if top.next != None :
            pq.enqueue(top.next)

    return dummy.next

def printList(node):
    while node is not None:
        print(node.val, end=" ")
        node = node.next


if __name__ == "__main__":
    k = 3

    arr = [None] * k

    arr[0] = Node(1)
    arr[0].next = Node(3)
    arr[0].next.next = Node(5)
    arr[0].next.next.next = Node(7)

    arr[1] = Node(2)
    arr[1].next = Node(4)
    arr[1].next.next = Node(6)
    arr[1].next.next.next = Node(8)

    arr[2] = Node(0)
    arr[2].next = Node(9)
    arr[2].next.next = Node(10)
    arr[2].next.next.next = Node(11)

    head = MergeKList(arr)

    printList(head)