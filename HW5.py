#HW 3
#Due Date: 02/01/2019, 11:59PM
########################################
#                                      
# Name: Hojin Ryoo
# Collaboration Statement: Madeline Rodriguez      
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
        cut = cut.replace('(', ' ')
        cut = cut.replace(')', ' ')
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
                    if isNumber(cut[:nextOpPos]) == True:
                        uno = float(cut[:nextOpPos])
                    elif isNumber(cut[:nnOpPos]) == True:
                        uno = float(cut[:nnOpPos])
                        nextOpPos = nnOpPos
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
    "^":3,
    "*":2,
    "/":2,
    "+":1,
    "-":1
    }
    #condition is whether the operator is within parenth
    condition = False
    operatorPos = 0
    while operatorPos != len(expr):
        prev = operatorPos - 1
        operand, operator, operatorPos = getNextNumber(expr, operatorPos)
        if prev == -1: 
            prev = operatorPos
        counter = 0
        if operatorPos != None:
            for x in range(operatorPos, 0, -1):
                if expr[x] == "(":
                    counter += 1
                elif expr[x] == ")":
                    counter -= 1
                else: 
                    continue
            if counter == 0: 
                condition = False
            else: 
                condition = True
            #next loop we need to start at the next number after the previous operator position
        else: 
            condition = False
        if operand == None: 
            return "error, invalid expression"
        else: 
            #We always append the operand to the post fix expression
            pfe.append(operand)
            #Last iteration, where there is no operator left
            if operator == None: 
                if s.isEmpty():
                    break
                else:
                    while len(s) != 0:
                        popped = s.pop()
                        pfe.append(popped)
                    break
            #if the stack is empty
            elif s.isEmpty():
                s.push(operator)
                ooo[prev] = ooo[operator]
            else: 
                if condition == True:
                    ooo[operatorPos] = 3 + counter
                    if ooo.get(operator) == None: 
                        return "error, invalid expression"
                    if ooo.get(operatorPos) == ooo.get(prev) and ooo.get(operator) < ooo.get(expr[prev]):
                        popped = s.pop()
                        pfe.append(popped)
                        s.push(operator)
                    elif ooo.get(operatorPos) > ooo.get(prev):
                        s.push(operator)
                    elif ooo.get(operatorPos) < ooo.get(prev):
                        popped = s.pop()
                        pfe.append(popped)
                        s.push(operator)
                    elif ooo.get(operatorPos) == ooo.get(prev) and ooo.get(operator) > ooo.get(expr[prev]):
                        s.push(operator)
                    else: 
                        popped = s.pop()
                        pfe.append(popped)
                        s.push(operator)
                # The operator is greater than the prev in terms of ooo
                elif ooo.get(operator) > ooo.get(prev): 
                    s.push(operator)
                    ooo[operatorPos] = ooo[operator]
                #The operator is less than the prev in terms of ooo and also does not have any parentheses
                elif ooo.get(operator) < ooo.get(prev) and ooo.get(prev) < 4:
                    while len(s) != 0:
                        popped = s.pop()
                        pfe.append(popped)
                    s.push(operator)
                    ooo[operatorPos] = ooo[operator]
                #The operator is less than the previous but has parentheses ooo
                elif ooo.get(operator) < ooo.get(prev):
                    popped = s.pop()
                    pfe.append(popped)
                    s.push(operator)
                    ooo[operatorPos] = ooo[operator]
                #The operators have equal ooo
                else: 
                    popped = s.pop()
                    pfe.append(popped)
                    s.push(operator)
                    ooo[operatorPos] = ooo[operator]
            operatorPos += 1
    final_solution = ""
    end = len(pfe) - 1
    for x, y in enumerate(pfe): 
        if x == end: 
            final_solution += str(y)
        else: 
            final_solution += str(y) + " "
    return final_solution

#current issue is if one of the numbers is negative7777777
def calculator(expr):
    # number of parenthesis check
    c = 0
    d = 0
    for x in expr: 
        if x == "(":
            c += 1
        elif x == ")":
            d += 1
        else: 
            continue
    if c != d: 
        return "error, invalid expression"
    pf_expr = postfix(expr)
    #postfix error check
    if pf_expr == "error, invalid expression":
        return "error, invalid expression"
    #Calculations
    while isNumber(pf_expr) == False:
        count = 0
        minuspos = 0
        realexpression = pf_expr
        counter = 0
        while True:
            if pf_expr[findNextOpr(pf_expr)] == "-":
                for indexing, element in enumerate(pf_expr): 
                    if element == "-":
                        minuspos = indexing
                        break
                    else: 
                        continue
                cut = pf_expr[minuspos+1:]
                for x in pf_expr[:minuspos+1]:
                    counter += 1
                if pf_expr[minuspos+1].isspace() == False: 
                    pf_expr = cut
                else: 
                    nextOpPos = counter - 1
                    break
            else: 
                nextOpPos = findNextOpr(pf_expr) + counter
                break
        pf_expr = realexpression
        operator = pf_expr[nextOpPos]
        index = nextOpPos
        #Traverses through the string negatively from the operator position
        while True: 
            index -= 1
            if count == 0:
                count += 1
            elif count == 1:
                newelement = pf_expr[index]
                if newelement.isspace() == True: 
                    operand2 = float(pf_expr[index:nextOpPos])
                    count += 1
                    index2 = index
                else: 
                    continue
            elif count == 2:
                newelement = pf_expr[index]
                if newelement.isspace() == True or index == 0: 
                    operand1 = float(pf_expr[index:index2])
                    count += 1
                else: 
                    continue
            else:
                break
        if operator == "/": 
            nfo = operand1 / operand2
        elif operator == "+":
            nfo = operand1 + operand2
        elif operator == "-":
            nfo = operand1 - operand2
        elif operator == "*":
            nfo = operand1 * operand2
        elif operator == "^":
            nfo = operand1 ** operand2
        else: 
            return "error, operator is not an operator"
        if index == -1:
            restofnumbers = ""
        else: 
            restofnumbers = pf_expr[:index+1]
        restofoperators = pf_expr[nextOpPos+1:]
        pf_expr = restofnumbers + " " + str(nfo) + restofoperators
    return float(pf_expr.strip())