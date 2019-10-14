#LAB 14
#Due Date: 04/05/2019, 11:59PM
########################################
#                                      
# Name: Hojin Ryoo
# Collaboration Statement:             
#
########################################


def bubbleSort(numList):
    '''
        Takes a list and returns 2 values
        1st returned value: a dictionary with the state of the list after each complete pass of bubble sort
        2nd returned value: the sorted list

        >>> bubbleSort([9,3,5,4,1,67,78])
        ({1: [3, 5, 4, 1, 9, 67, 78], 2: [3, 4, 1, 5, 9, 67, 78], 3: [3, 1, 4, 5, 9, 67, 78], 4: [1, 3, 4, 5, 9, 67, 78], 5: [1, 3, 4, 5, 9, 67, 78]}, [1, 3, 4, 5, 9, 67, 78])
    '''
    # Your code starts here
    if type(numList)!= list: 
        return "error, input is not a list"
    for x in numList:
    	if type(x) != int:
    		return "error, element is not an integer"
    	else: 
    		continue
    pass_number = 0
    swapped = True
    exit_index = len(numList) -1
    current_status = {}
    swapped_counter = 0
    while swapped != False:
        pass_number += 1
        for index, element in enumerate(numList):
            if index == exit_index:
                break
            elif element > numList[index+1]:
                numList[index], numList[index+1] = numList[index+1], numList[index]
                current_status[pass_number]=numList[:]
                swapped_counter += 1
            else: 
                continue 
        if swapped_counter == 0: 
            current_status[pass_number]=numList[:]
            swapped = False
        else: 
            swapped = True
            swapped_counter = 0
    return (current_status, numList)