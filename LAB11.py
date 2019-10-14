#Lab #11
#Due Date: 03/15/2019, 11:59PM
########################################
#                                      
# Name:
# Collaboration Statement:             
#  
########################################

class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                        
                          
class Queue:
    '''
        >>> x=Queue()
        >>> x.isEmpty()
        True
        >>> x.dequeue()
        'Queue is empty'
        >>> x.enqueue(1)
        >>> x.enqueue(2)
        >>> x.enqueue(3)
        >>> x.dequeue()
        1
        >>> print(x)
        Head:Node(2)
        Tail:Node(3)
        Queue:2 3
    '''
    def __init__(self): 
        self.head=None
        self.tail=None

    def __str__(self):
        temp=self.head
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out=' '.join(out)
        return ('Head:{}\nTail:{}\nQueue:{}'.format(self.head,self.tail,out))

    __repr__=__str__

    def isEmpty(self):
        if self.head == None: 
            return True
        else: 
            return False

    def __len__(self):
        count = 0
        origin = self.head
        while self.head != None: 
            count += 1
            self.head = self.head.next
        self.head = origin
        return count

    def enqueue(self, value):
        if self.tail == None: 
            self.tail = Node(value)
            self.head = self.tail
        else: 
            self.tail.next = Node(value)
            self.tail = self.tail.next

    def dequeue(self):
        if self.head == None: 
            return "Queue is empty"
        deqNode = self.head
        self.head = self.head.next
        if self.head == None: 
            self.tail = None
        return deqNode.value
