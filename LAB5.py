#Lab #5
#Due Date: 02/08/2019, 11:59PM
########################################
#                                      
# Name: Hojin Ryoo
# Collaboration Statement: I did not work with anyone!          
#
########################################

import math

class SodaMachine:
    '''
        >>> m = SodaMachine('Coke', 10)
        >>> m.purchase()
        'Product out of stock'
        >>> m.restock(2)
        'Current soda stock: 2'
        >>> m.purchase()
        'Please deposit $10'
        >>> m.deposit(7)
        'Balance: $7'
        >>> m.purchase()
        'Please deposit $3'
        >>> m.deposit(5)
        'Balance: $12'
        >>> m.purchase()
        'Coke dispensed, take your $2'
        >>> m.deposit(10)
        'Balance: $10'
        >>> m.purchase()
        'Coke dispensed'
        >>> m.deposit(15)
        'Sorry, out of stock. Take your $15 back'
    '''
    def __init__(self, product, price):
    #-- start code here ---
        self.product = product
        self.price = price
        self.depo = 0
        self.stock = 0

    def purchase(self):
    #-- start code here ---
        if self.stock == 0: 
            return "Product out of stock"
        else: 
            if self.deposit == 0:
                return "Please deposit $" + str(self.price)
            elif self.depo < self.price: 
                return "Please deposit $" + str(self.price - self.depo)
            elif self.depo > self.price: 
                remainder = self.depo - self.price
                self.depo = 0
                self.stock -= 1
                return self.product + " dispensed, take your $" + str(remainder)
            else: 
                self.depo = 0
                self.stock -= 1
                return self.product + " dispensed"

    def deposit(self, amount):
    #-- start code here ---
        self.depo += amount
        if self.stock == 0: 
            return "Sorry, out of stock. Take your $" + str(amount) + " back"
        else: 
            return "Balance: $" + str(self.depo)

    def restock(self, amount):
    #-- start code here ---
        self.stock += amount
        return "Current soda stock: " + str(self.stock)
    

class Line:
    ''' 
        Creates objects of the class Line, takes 2 tuples. Class must have 2 PROPERTY methods
        >>> line1=Line((-7,-9),(1,5.6))
        >>> line1.distance
        16.648
        >>> line1.slope
        1.825
        >>> line2=Line((2,6),(2,3))
        >>> line2.distance
        3.0
        >>> line2.slope
        'Infinity'
    '''


    def __init__(self, coord1, coord2):
    #-- start code here ---
        self.x1 = coord1[0]
        self.y1 = coord1[1]
        self.x2 = coord2[0]
        self.y2 = coord2[1]
    
    @property
    def distance(self):
    #-- start code here ---
        d = math.sqrt((self.x2-self.x1)**2 + (self.y2-self.y1)**2) 
        d = round(d, 3)
        return d
    #-- ends here ---
    
    @property
    def slope(self):
    #-- start code here ---
        num = self.y2 - self.y1
        denom = self.x2 - self.x1
        if denom == 0: 
            return "Infinity"
        s = (num)/(denom)
        s = round(s, 3)
        return s
    #-- ends here ---