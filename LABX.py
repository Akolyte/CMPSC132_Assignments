#Lab #12
#Due Date: 03/22/2019, 11:59PM
########################################
#                                      
# Name: Hojin Ryoo
# Collaboration Statement:             
#  
########################################

import math as m

class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                        
                          
class Stack:
    '''
        >>> x=Stack()
        >>> x.pop()
        'Stack is empty'
        >>> x.push(2)
        >>> x.push(4)
        >>> x.push(6)
        >>> x
        Top:Node(6)
        Stack:
        6
        4
        2
        >>> x.pop()
        6
        >>> x
        Top:Node(4)
        Stack:
        4
        2
        >>> len(x)
        2
        >>> x.peek()
        4
    '''
    def __init__(self):
        self.top = None
    
    def __str__(self):
        temp=self.top
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out='\n'.join(out)
        return ('Top:{}\nStack:\n{}'.format(self.top,out))

    __repr__=__str__
    
    def isEmpty(self):
        if self.top == None: 
            return True
        else:
            return False

    def __len__(self):
        count = 0
        origin = self.top
        while self.top != None: 
            count += 1
            self.top = self.top.next
        self.top = origin
        return count
    
    def peek(self):
        return self.top.value

    def push(self,value):
        if self.top == None:
            self.top = Node(value)
        else: 
            nextNode = self.top
            self.top = Node(value)
            self.top.next = nextNode

    def pop(self):
        if self.top == None: 
            return "Stack is empty"
        if self.top.next == None: 
            poppedNode = self.top
            self.top = None
            return poppedNode.value
        poppedNode = self.top
        self.top = self.top.next
        return poppedNode.value

class MaxHeapPriorityQueue:
    '''
        >>> h = MaxHeapPriorityQueue()
        >>> h.insert(10)
        >>> h.insert(5)
        >>> h.heap
        [10, 5]
        >>> h.insert(14)
        >>> h.heap
        [14, 5, 10]
        >>> h.insert(9)
        >>> h.heap
        [14, 9, 10, 5]
        >>> h.insert(2)
        >>> h.heap
        [14, 9, 10, 5, 2]
        >>> h.insert(11)
        >>> h.heap
        [14, 9, 11, 5, 2, 10]
        >>> h.insert(6)
        >>> h.heap
        [14, 9, 11, 5, 2, 10, 6]
        >>> h.parent(2)
        14
        >>> h.leftChild(1)
        9
        >>> h.rightChild(1)
        11
        >>> h.deleteMax()
        14
        >>> h.heap
        [11, 9, 10, 5, 2, 6]
        >>> h.deleteMax()
        11
        >>> h.heap
        [10, 9, 6, 5, 2]
    '''

    def __init__(self):
        self.heap=[]
        self.size = 0

    def __len__(self):
        count = 0
        for x in self.heap: 
            count += 1
        return count

    def parent(self,index):
        if index <= 1 or index > self.size: 
            return None
        else: 
            pIndice = m.floor(index/2)
            return self.heap[pIndice-1]

    def leftChild(self,index):
        if index < 1 or index > self.size: 
            return None
        else: 
            leftIndice = 2*index
            try: 
                return self.heap[leftIndice-1]
            except:
                return None

    def rightChild(self,index):
        if index < 1 or index > self.size: 
            return None
        else: 
            rightIndice = 2*index+1
            try:
                return self.heap[rightIndice-1]
            except:
                return None

    def swap(self, index1, index2):
        self.heap[index1-1], self.heap[index2-1] = self.heap[index2-1], self.heap[index1-1]
        
    def insert(self,x):
        self.heap
        self.heap.append(x)
        self.size += 1
        xIndice = len(self.heap)
        pIndice = m.floor(xIndice/2)
        while True: 
            #breaks if there is no parent index
            if pIndice-1 == -1: 
                break
            if self.heap[pIndice-1] <= self.heap[xIndice-1]: 
                self.swap(xIndice, pIndice)
                xIndice = pIndice
                pIndice = m.floor(xIndice/2)
            #breaks if there is no reason to swap nodes
            else: 
                break

    def deleteMax(self):
        if self.size<=0:
            return None
        elif self.size==1:
            self.size=0
            return self.heap[0]
        else: 
            #Save the root
            popped = self.heap[0]
            #Remove Root 
            #Move the rightmost leaf
            xIndice = len(self.heap)
            self.swap(xIndice, 1)
            del self.heap[xIndice-1]
            self.size -= 1
            #Find the biggest child
            #swap node with biggest child
            pIndice = 1
            while True:
                if self.leftChild(pIndice) == None and self.rightChild(pIndice) == None:
                    return popped
                #if both children exist, continue
                if self.leftChild(pIndice) != None and self.rightChild(pIndice) != None:
                    #if either child is greater than the parent
                    if self.leftChild(pIndice) > self.heap[pIndice-1] or self.rightChild(pIndice) > self.heap[pIndice-1]:
                        #if the left child is greater than the right child
                        if self.leftChild(pIndice) > self.rightChild(pIndice):
                            leftIndice = 2*pIndice
                            self.swap(pIndice, leftIndice)
                            pIndice = leftIndice
                            continue
                        #if the right child is greater than the left child
                        elif self.leftChild(pIndice) < self.rightChild(pIndice):
                            rightIndice = 2*pIndice+1
                            self.swap(pIndice, rightIndice)
                            pIndice = rightIndice
                            continue
                        #if the left child is equal to the right child
                        elif self.leftChild(pIndice) == self.rightChild(pIndice):
                            leftIndice = 2*pIndice
                            self.swap(pIndice, leftIndice)
                            pIndice = leftIndice
                        else: 
                            continue
                    else: 
                        break
                elif self.leftChild(pIndice) != None: 
                    leftIndice = 2*pIndice
                    if self.heap[pIndice-1] < self.heap[leftIndice-1]:
                        self.swap(pIndice, leftIndice)
                        pIndice = leftIndice
                        return popped
                    return popped
                elif self.rightChild(pIndice) != None:
                    rightIndice = 2*pIndice+1
                    if self.heap[pIndice-1] < self.heap[rightIndice-1]:
                        self.swap(pIndice, rightIndice)
                        pIndice = rightIndice
                        return popped
                    return popped
                else: 
                    break
            return popped

def heapSort(numList):
    #assign h to a maxheap
    h = MaxHeapPriorityQueue()
    #iterate through numList and insert into heap
    for x in numList: 
        h.insert(x)
    #assing heap to newList
    newList = h.heap
    #create stack to reverse order
    s = Stack()
    #take the highest value and push into stack to reverse order of heap
    while h.size != 0: 
        popped = h.deleteMax()
        s.push(popped)
    newList = []
    while len(s) != 0:
        popped = s.pop()
        newList.append(popped)
    return newList