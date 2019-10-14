#Lab #10
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