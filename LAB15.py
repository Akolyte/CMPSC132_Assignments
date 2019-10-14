#LAB 15
#Due Date: 04/05/2019, 11:59PM
########################################
#                                
# Name:
# Collaboration Statement:             
#
########################################

def merge(list1, list2):
    '''
        >>> merge([12,26,35,87],[7,9,28])
        [7, 9, 12, 26, 28, 35, 87]
        >>> merge([12,35],[26,87])
        [12, 26, 35, 87]
    '''
    #write your code here
    if type(list1) != list or type(list2) != list:
        return "error, an input is not a list or an element of the list is not a number"
    for x in list1:
        if type(x) != int and type(x) != float:
            return "error, an element of the list is not a number"
    for y in list2: 
        if type(y) != int and type(y) != float:
            return "error, an element of the list is not a number"
    newList = []
    index_length = len(list1)
    index_length2 = len(list2)
    i = 0
    j = 0
    #loops for as long as i and j do not go out of index
    while i < index_length and j < index_length2:
        #if the element of list1 is less than or equal to the element
        #of list2, append the element of list1 to the newList and go to the next element of list1
        if list1[i] <= list2[j]:
            newList.append(list1[i])
            i += 1
        #opposite of the above
        else: 
            newList.append(list2[j])
            j += 1
    #append the leftovers of each list to the newList one list should be leftover only
    for x in list1[i:]:
        newList.append(x)
    for y in list2[j:]:
        newList.append(y)
    return newList

def mergeSort(numList):
    '''
       >>> mergeSort([12,35,87,26,9,28,7])
       [7, 9, 12, 26, 28, 35, 87]
    '''
    #write your code here
    if type(numList) != list:
        return "input is not a list"
    else:
        if len(numList) == 0: 
            return numList
        elif len(numList) == 1:
            return numList
        else:
            midpoint = len(numList)//2
            left = mergeSort(numList[:midpoint])
            right = mergeSort(numList[midpoint:])
            numList = merge(left, right)
            return numList