#Lab #12
#Due Date: 03/22/2019, 11:59PM
########################################
#                                      
# Name: Hojin Ryoo
# Collaboration Statement:             
#  
########################################

import math as m

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
            if leftIndice < 1 or leftIndice > self.size: 
                return None
            else:
                return self.heap[leftIndice-1]

    def rightChild(self,index):
        if index < 1 or index > self.size: 
            return None
        else: 
            rightIndice = 2*index+1
            if rightIndice < 1 or rightIndice > self.size:
                return None
            else:
                return self.heap[rightIndice-1]

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
                if self.leftChild(pIndice) != None and self.rightChild(pIndice) != None:
                    if self.leftChild(pIndice) > self.heap[pIndice-1] or self.rightChild(pIndice) > self.heap[pIndice-1]:
                        if self.leftChild(pIndice) > self.rightChild(pIndice):
                            leftIndice = 2*pIndice
                            self.swap(pIndice, leftIndice)
                            pIndice = leftIndice
                            continue
                        elif self.leftChild(pIndice) < self.rightChild(pIndice):
                            rightIndice = 2*pIndice+1
                            self.swap(pIndice, rightIndice)
                            pIndice = rightIndice
                            continue
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
                    self.swap(pIndice, leftIndice)
                    pIndice = leftIndice
                elif self.rightChild(pIndice) != None:
                    rightIndice = 2*pIndice+1
                    self.swap(pIndice, rightIndice)
                    pIndice = rightIndice
                else: 
                    break
            return popped