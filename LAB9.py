#Lab #9
#Due Date: 03/01/2019, 11:59PM
########################################
#                                      
# Name: Hojin Ryoo
# Collaboration Statement: Kelly Cooper            
#  
########################################


class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                        

                          
class OrderedLinkedList:
    '''
        >>> x=OrderedLinkedList()
        >>> x.pop()
        'List is empty'
        >>> x.add(-6)
        >>> x.add(8)
        >>> x.add(3)
        >>> x.add(7)
        >>> print(x)
        Head:Node(8)
        Tail:Node(-6)
        List:8 7 3 -6
        >>> len(x)
        4
        >>> x.pop()
        -6
        >>> print(x)
        Head:Node(8)
        Tail:Node(3)
        List:8 7 3
    '''
    def __init__(self):
    	#You can add a count attribute for len
        self.head=None
        self.tail=None

    def __str__(self):
        temp=self.head
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out=' '.join(out)
        return ('Head:{}\nTail:{}\nList:{}'.format(self.head,self.tail,out))

    __repr__=__str__

    def add(self, value):
        #write your code here
        #Case where data structure is empty
        new_node = Node(value)
        if self.head == None: 
            self.head = new_node
            self.tail = new_node
            return None
        #Case where data structure has nodes
        temp = self.head
        prev = temp
        #Finding where to place the node
        while True: 
            #If temp is accessing the first node
            if temp == None:
                break
            if temp.value > value and temp == self.head: 
                temp = temp.next
            #If the value is less than the current nodes value we continue
            elif temp.value > value:
                temp = temp.next
                prev = prev.next
            #If inserting and there are no other nodes left.
            else: 
                break
        #Assigning the Node
        #Case where we're assigning the node to the beginning
        if temp == prev: 
            new_node.next = temp
            self.head = new_node
        #Case where we're placing the node at middle
        elif temp != prev and temp != None: 
            new_node.next = temp
            prev.next = new_node
        #Case where we're placing at the end
        else:
            new_node.next = None
            prev.next = new_node
            self.tail = new_node
    
    #something wrong with pop or adding to the middle
    def pop(self):
        #write your code here
        if self.head == None: 
            return "List is empty"
        temp = self.head
        prev = temp 
        if temp == self.tail: 
            self.head = None
            self.tail = None
            return temp.value
        temp = temp.next
        while temp != self.tail: 
            temp = temp.next
            prev = prev.next
        self.tail = prev
        prev.next = None
        return temp.value

    def isEmpty(self):
        #write your code here
        if self.head == None: 
            return True
        else: 
            return False

    def __len__(self):
        #write your code here
        count = 0
        temp = self.head
        while temp != None: 
            temp = temp.next
            count += 1
        return count