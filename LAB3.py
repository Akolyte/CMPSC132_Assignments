#Lab #3
#Due Date: 01/25/2019, 11:59PM
########################################
#                                      
# Name: Hojin Ryoo
# Collaboration Statement:             
#
########################################

def countWords(txt):
    """
        >>> article1='''
        ... He will be the president of the company; right now
        ... he's a vice president.
        ... But he ..... himself,  is no sure of it...
        ... (Later he will see the importance of these 3.)
        ... '''
        >>> expected={'he': 3,"he's": 1, 'will': 2, 'be': 1, 'the': 3, 'president': 2, 'of': 3, 'company': 1, 'right': 1, 'now': 1, 'is': 1, 'a': 1, 'vice': 1, 'but': 1, 'himself': 1, 'no': 1, 'sure': 1, 'it': 1, 'later': 1, 'see': 1, 'importance': 1, 'these': 1}
        >>> countWords(article1)==expected
        True
        >>> countWords(55)
        'error'
        >>> countWords([3.5,6])
        'error'

    """
    # --- YOU CODE STARTS HERE
    if type(txt) != str: 
        return "error"
    else: 
        #Creates dictionary, filters out punctuation, and then creates a list of words
        wDict = {}
        for x, y in enumerate(txt):
            if y.isalpha() == False and y != "'": 
                txt = txt[:x] + " " + txt[x+1:]
            else: 
                continue
        txt = txt.lower()
        wList = txt.split()
        #Creates entry for every word
        for u in wList: 
            wDict[u] = 0
        #Counts number of words for each entry and updates dictionary
        for u in wList: 
            for key, value in wDict.items():
                if  key == u: 
                    wDict[key] = value + 1
                else: 
                    continue
        return wDict


def studentGrades(gradeList):
    """
        >>> grades = [
        ...     ['Student', 'Quiz 1', 'Quiz 2', 'Quiz 3'],
        ...     ['John', 100, 90, 80],
        ...     ['McVay', 88, 99, 111],
        ...     ['Rita', 45, 56, 67],
        ...     ['Ketan', 59, 61, 67],
        ...     ['Saranya', 73, 79, 83],
        ...     ['Min', 89, 97, 101]]
        >>> studentGrades(grades)
        [90, 99, 56, 62, 78, 95]
        >>> grades = [
        ...     ['Student', 'Quiz 1', 'Quiz 2'],
        ...     ['John', 100, 90],
        ...     ['McVay', 88, 99],
        ...     ['Min', 89, 97]]
        >>> studentGrades(grades)
        [95, 93, 93]
        >>> studentGrades(55)
        'error'
    """
    # --- YOU CODE STARTS HERE
    if type(gradeList) != list: 
        return "error"
    else: 
        gList = []
        del gradeList[0]
        for x in gradeList: 
            del x[0]
            count = 0
            for y in x:
                count += 1
            q = sum(x)//count
            gList.append(q)
        return gList