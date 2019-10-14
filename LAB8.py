#Lab #8
#Due Date: 02/22/2019, 11:59PM
########################################
#                                      
# Name: Hojin Ryoo
# Collaboration Statement: None            
#
########################################


def isPrime(n, i = 2):
    '''
        >>> isPrime(5)
        True
        >>> isPrime(1)
        False
        >>> isPrime(9)
        False
        >>> isPrime(85)
        False
        >>> isPrime(1019)
        True
    '''
    # --- Your code starts here
    #Base case 1
    if n == 1: 
        return False
    else: 
        #Base Case 2
        if i > n**(1/2): 
            return True
        #Break
        elif n % i == 0: 
            return False
        #finding the countup
        else: 
            return isPrime(n, i+1)