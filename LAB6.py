#Lab #6
#Due Date: 02/08/2019, 11:59PM
########################################
#                                      
# Name: Hojin Ryoo
# Collaboration Statement: I did not work with anyone!            
#
########################################


class Vector:
    '''
        >>> Vector([1,2])+Vector([5])
        'Error - Invalid dimensions'
        >>> Vector([1,2])+Vector([5,2])
        Vector([6, 4])
        >>> Vector([1,2])-Vector([5,2])
        Vector([-4, 0])
        >>> Vector([1,2])*Vector([5,2])
        9
        >>> x=Vector([2,4,6])
        >>> y=Vector([2,4,6])
        >>> c=x+y
        >>> type(c)
        <class 'LAB6.Vector'>
        >>> print(c)
        Vector([4, 8, 12])
        >>> x==y
        True
        >>> x-Vector([1,2])
        'Error - Invalid dimensions'
        >>> x+5
        'Error - Invalid operation'
        >>> x*y
        56
        >>> x*5
        Vector([10, 20, 30])
        >>> 5*x
        Vector([10, 20, 30])
    '''

    def __init__(self, vector_list):
        self.vector = vector_list

    # --- Your code starts here
    #addition
    def __add__(self, other):
        if type(self) == int or type(other) == int:
            return "Error - Invalid operation"
        if len(self.vector) != len(other.vector):
            return "Error - Invalid dimensions"
        nVector = []
        entry = 0
        for x in range(0, len(self.vector)):
            entry = self.vector[x] + other.vector[x]
            nVector.append(entry)
        m = Vector(nVector)
        return m
    #subtraction
    def __sub__(self, other):
        if type(self) == int or type(other) == int:
            return "Error - Invalid operation"
        if len(self.vector) != len(other.vector):
            return "Error - Invalid dimensions"
        nVector = []
        entry = 0
        for x in range(0, len(self.vector)):
            entry = self.vector[x] - other.vector[x]
            nVector.append(entry)
        m = Vector(nVector)
        return m
    #dot product
    def __mul__(self, other):
        if type(other) == int: 
            nVector = []
            entry = 0
            for x in range(0, len(self.vector)):
                entry = self.vector[x] * other
                nVector.append(entry)
            m = Vector(nVector)
            return m
        if len(self.vector) != len(other.vector):
            return "Error - Invalid dimensions"
        total = 0
        addsum = 0
        for x in range(0, len(self.vector)):
            addsum = self.vector[x] * other.vector[x]
            total += addsum
        return total
    #scalar
    def __rmul__(self, other):
        nVector = []
        entry = 0
        for x in range(0, len(self.vector)):
            entry = self.vector[x] * other
            nVector.append(entry)
        m = Vector(nVector)
        return m
    #equality
    def __eq__(self, other):
        for x in range(0, len(self.vector)):
            if self.vector[x] == other.vector[x]:
                continue
            else: 
                return False
        return True
    #Change the format of return 
    def __repr__(self):
        return "Vector(" + str(self.vector) + ")"

    def __str__(self):
        return "Vector(" + str(self.vector) + ")"