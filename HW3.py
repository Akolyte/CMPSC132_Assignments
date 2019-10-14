#HW 3
#Due Date: 02/01/2019, 11:59PM
########################################
#                                      
# Name: Hojin Ryoo
# Collaboration Statement:            
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
                #attempt to turn the previous negative sign and number into a float
                #should it succeed, we store the number, and the position of the 2nd operator as the 1st
                if nnOpPos == -1:
                    try: 
                        uno = float(cut[:nextOpPos])
                    #Unique Case where the nextOpPos will not technically be none unless changed!
                    except ValueError: 
                        uno = float(cut[nextOpPos:])
                        nextOpPos = -1
                else:
                    if isNumber(cut[:nnOpPos+1]) == True:
                        try: 
                            uno = float(cut[:nnOpPos+1])
                            nextOpPos = nnOpPos+2
                        except ValueError: 
                            uno = float(cut[:nextOpPos+1])
                    else:
                        uno = None
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