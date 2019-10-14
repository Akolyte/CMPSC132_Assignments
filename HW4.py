#HW 3
#Due Date: 02/01/2019, 11:59PM
########################################
#                                      
# Name: Hojin Ryoo
# Collaboration Statement: Kelly Cooper         
#
########################################


def findNextOpr(txt):
    """
        >>> findNextOpr('  3*   4 - 5')
        3
        >>> findNextOpr('8   4 - 5')
        6
        >>> findNextOpr('89 4 5')
        -1
    """
    if not isinstance(txt,str) or len(txt)<=0:
        return "error: findNextOpr"

    # --- YOU CODE STARTS HERE
    else: 
        #Create List of Operators to compare
        opList = ["+", "-", "/","*", "^"]
        #Iterate through the string, and compare with the list to see if each character is an operator
        for x, y in enumerate(txt): 
            for z in opList:
                if y == z: 
                    return x
        return -1



def isNumber(txt):
    """
        >>> isNumber('1   2 3')
        False
        >>> isNumber('-  156.3')
        False
        >>> isNumber('     29.99999999    ')
        True
        >>> isNumber('    5.9999x ')
        False
    """
    if not isinstance(txt, str) or len(txt)==0:
        return "error: isNumber"
    # --- YOU CODE STARTS HERE
    else: 
        try: 
            m = float(txt)
            return True
        except ValueError: 
            return False

def getNextNumber(expr, pos):
    """
        >>> getNextNumber('8  +    5    -2',0)
        (8.0, '+', 3)
        >>> getNextNumber('8  +    5    -2',4)
        (5.0, '-', 13)
        >>> getNextNumber('4.5 + 3.15         /  -5',20)
        (-5.0, None, None)
        >>> getNextNumber('4.5 + 3.15         /   5',10)
        (None, '/', 19)
    """

    if not isinstance(expr, str) or not isinstance(pos, int) or len(expr)==0 or pos<0 or pos>=len(expr):
        return None, None, "error: getNextNumber"
    # --- YOU CODE STARTS HERE
    else:
        #Cuts the string from pos
        cut = expr[pos:]
        #picks up remainder of position for expr for later use
        count = 0
        for x in expr[:pos]:
            count += 1
        #finds the position of the next operator within the cut string
        nextOpPos = findNextOpr(cut)
        #1st Result
        #if there is no operator, try to take the segment and turn it into a float. 
        #If it succeeds, store it. If it fails, store None. 
        if nextOpPos == -1:
            try:
                uno = float(cut)
            except ValueError:
                uno = None
        #In the case that there is a negative number, we need to be able to skip the negative sign
        #check the next operator, try to turn the previous part into a float, and store results accordingly.
        else: 
            if cut[nextOpPos] == "-":
                #finds next next operator
                nnOpPos = findNextOpr(cut[nextOpPos+1:])
                #if there is no next operator after -
                if nnOpPos == -1: 
                    try:
                        uno = float(cut[:nextOpPos])
                    except ValueError: 
                        uno = float(cut[nextOpPos:])
                        nextOpPos = -1
                #attempt to turn the previous negative sign and number into a float
                #should it succeed, we store the number, and the position of the 2nd operator as the 1st
                else:
                    if isNumber(cut[:nnOpPos]) == True:
                        uno = float(cut[:nnOpPos])
                        nextOpPos = nnOpPos + 1
                    else:
                        uno = float(cut[:nextOpPos + nnOpPos + 1])
                        nextOpPos += nnOpPos + 1
            else:
                if isNumber(cut[:nextOpPos]) == True:
                    uno = float(cut[:nextOpPos])
                else: 
                    uno = None
        #2nd Result and 3rd result
        #We return the next operator
        #If there is no operator, we return none for operator and pos of operator
        if nextOpPos == -1:
            dos = None
            tres = None
        #if there is an operator, we find it through indexing the cut
        else: 
            dos = cut[nextOpPos]
            tres = nextOpPos + count
        return (uno, dos, tres)
        
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

def postfix(expr): 
    if expr[-1] == "+" or expr[-1] == "-" or expr[-1] == "/" or expr[-1] == "*":
        return "error, invalid expression"
    s = Stack()
    #post fix expression
    pfe = []
    #order of operations
    ooo = {
    "^":1,
    "*":2,
    "/":2,
    "+":3,
    "-":3
    }
    tres = 0
    count = 0
    while tres != len(expr):
        #uno is the operand before the operator
        #dos is the operator
        #tres is the position of the operator in the string
        uno, dos, tres = getNextNumber(expr, tres)
        #next loop we need to start at the next number, not at the next operator
        if uno == None: 
            return "error, invalid expression"
        else: 
            pfe.append(uno)
            if dos == None: 
                if s.isEmpty():
                    break
                else:
                    popped = s.pop()
                    pfe.append(popped)
                    break
            elif s.isEmpty():
                s.push(dos)
            else: 
                if ooo.get(dos) < ooo.get(s.peek()): 
                    s.push(dos)
                elif ooo.get(dos) > ooo.get(s.peek()):
                    while len(s) != 0:
                        popped = s.pop()
                        pfe.append(popped)
                    s.push(dos)
                else: 
                    popped = s.pop()
                    s.push(dos)
                    pfe.append(popped)
            count += 1
            tres += 1
    final_solution = ""
    end = len(pfe) - 1
    for x, y in enumerate(pfe): 
        if x == end: 
            final_solution += str(y)
        else: 
            final_solution += str(y) + " "
    return final_solution