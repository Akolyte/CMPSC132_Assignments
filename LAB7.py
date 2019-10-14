#Lab #7
#Due Date: 02/22/2019, 11:59PM
########################################
#                                      
# Name: Hojin Ryoo
# Collaboration Statement: None           
#
########################################



#### DO NOT modify the triangle(n) function in any way! 
def triangle(n):
    return recursive_triangle(n, n)

###################

def recursive_triangle(k, n):
    '''
        >>> recursive_triangle(2,4)
        '  **\\n   *'
        >>> print(recursive_triangle(2,4))
          **
           *
        >>> triangle(4)
        '****\\n ***\\n  **\\n   *'
        >>> print(triangle(4))
        ****
         ***
          **
           *
    '''
    # --- YOUR CODE STARTS HERE
    count = k
    if count == 1: 
        return (" " * (n - k)) + "*"
    else: 
        count -= 1
        pizza = count + 1
        return " " * (n - pizza) + ("*"*(pizza)) + "\n" + recursive_triangle(count, n)