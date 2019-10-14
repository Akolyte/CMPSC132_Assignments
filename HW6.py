#HW 6
#Due Date: 04/26/2019, 11:59PM
########################################
#
# Name: Hojin Ryoo
# Collaboration Statement:
#
########################################

# ---Copy your code from labs 10 and 11 here (you can remove their comments)  
class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__

class Queue:
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

class Stack:
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

#----- HW6 Graph code     
class Graph:
    def __init__(self, graph_repr):
        self.vertList = graph_repr

    def bfs(self, start):
        # Your code starts here
        #CATCHING ERRORS
        if type(start) != str:
            return "error, starting node was not entered as a string"
        if start not in self.vertList:
            return "error, starting node is not in the graph"
        q = Queue()
        vList = []
        #Add the first node to the queue and the verticeList
        q.enqueue(start)
        visited = start
        vList.append(start)
        while q.isEmpty() != True:
            #Remove an item from q, its neighbors will be visited now
            node = q.dequeue()
            #Creates a temperary list to store values to be sorted before inserting into verticeList
            tempList = []
            #Finds all of the neighbors of the node
            for x in self.vertList.get(node):
                #Case where weights are involved
                if type(x) == tuple:
                    if x[0] not in vList:
                        visited = x[0]
                        tempList.append(visited)
                #Case where there are no weights
                elif type(x) == str:
                    if x not in vList:
                        visited = x
                        tempList.append(visited)
            #Finds alphabetical order of the neighbors to traverse
            tempList = sorted(tempList)
            travDict = 0
            while len(tempList) != 0:
                visited = tempList[0]
                vList.append(visited)
                q.enqueue(visited)
                del tempList[0]
        return vList

    def dfs(self, start):
        # Your code starts here
        #CATCHING ERRORS
        if type(start) != str:
            return "error, node was not entered as a string"
        if start not in self.vertList:
            return "error, node is not in the graph"
        #Let s be an empty stack
        vList = []
        s = Stack()
        s.push(start)
        visited = start
        vList.append(start)
        while s.isEmpty() != True: 
            #Pop a node from stack to visit next
            node = s.pop()
            if node not in vList:
                vList.append(node)
            #Creates temperary list to sort alphabetically
            tList = []
            tweight = {}
            #Finds all of the neighbors of the node
            for x in self.vertList.get(node):
                #Case where weights are involved
                if type(x) == tuple:
                    if x[0] not in vList:
                        visited = x[0]
                        weight = x[1]
                        tList.append(visited)
                        tweight[visited] = weight
                #Case where there are no weights
                elif type(x) == str:
                    if x not in vList:
                        visited = x
                        tList.append(visited)
            #List of neighbors of current node
            tList = sorted(tList, reverse=True)
            if len(tweight) == 0: 
                for x in tList:
                    if x not in vList:
                        s.push(x)
            else: 
                while len(tList) != 0:
                    visited = tList[0]
                    if visited not in vList:
                        s.push(visited)
                        del tList[0]
        return vList

    ### EXTRA CREDIT, uncomment method definition if submitting extra credit
    
    #def dijkstra(self,start):
        # Your code starts here