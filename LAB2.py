#Lab #2
#Due Date: 01/25/2019, 11:59PM
########################################
#                                      
# Name: Hojin Ryoo
# Collaboration Statement:             
#
########################################


def joinedList(n):
    """
        >>> joinedList(5)
        [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
        >>> joinedList(-3)
        [-3, -2, -1, -1, -2, -3]
        >>> joinedList('5')
        'error'
        >>> joinedList([2,8,[9]])
        'error'
        >>> joinedList(0)
        []
    """
    # --- YOU CODE STARTS HERE
    jList = []
    countdown = 0
    if type(n) != int: 
        return "error"
    elif n > 0: 
        for x in range(1, n+1):
            jList.append(x)
            countdown += 1
        for y in range(1, n+1):
            jList.append(countdown)
            countdown -= 1
        return jList
    elif n < 0:
        countdown = n-1
        for x in range(n, 0):
            jList.append(x)
            countdown += 1
        for y in range(n, 0):
            jList.append(countdown)
            countdown -= 1
        return jList
    else:
        return jList

def removePunctuation(txt):
    """
        # txt : string
        # It replaces every character that is not an alphabet letter
        # into a space, and returns it.

        >>> removePunctuation("I like chocolate cake!!(!! It's the best flavor..;.$ for real")
        'I like chocolate cake      It s the best flavor      for real'
        >>> removePunctuation("Dots...................... many dots..X")
        'Dots                       many dots  X'
        >>> removePunctuation(55)
        'error'
        >>> removePunctuation([3.5,6])
        'error'

    """
    # --- YOU CODE STARTS HERE
    if type(txt) != str: 
        return "error"
    else: 
        for x, y in enumerate(txt): 
            if y.isalpha() == True: 
                continue
            elif y.isalpha() == False: 
                txt = txt[:x] + " " + txt[x+1:]
        return txt