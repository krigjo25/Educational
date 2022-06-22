'''
Chapter 0: Object Oriented Programming Part 1

Question 1 :

class Car:

    def__init__(self, pMake, pModel, pColor, pPrice):
        self.make = pMake
        self.model = pModel
        self.color = pColor
        self.price = pPrice

    def__str__(self):
    return 'Make = %s, Model = %s, Color = %s, Price = %s' % (self.make, self.model, self.color, self.price)

    def selectColor(self):
    self.color = input('Choose the new color :')

    def calculateTax(self):
        priceWithTax = 1.1*self.price
        return pricewithTax

Question 1.1 :

make = 'Honda'
model = 'Civic'
Color = 'white'
price = '15000'

Question 1.2 :

    print a string representation of myFirstCar using the __str__ method the output should
    be :

    Brand = Honda, model = Civic, Color = white, Price = 15000


Question 1.3 :

Update the price of MyFirstCar to 18000 and print a string representation of it again.

Qustion 1.4 :
Update the color of MyFirstCar to "Orange" using the selectColor() method and print a string
representation to a variable called finalPrice. Print the value of finalPrice


'''
class VehicleImport:
    
    company = 'Vehicle import AD'
    '''
        *  __init__ creates a class with the most common things
    '''
    def __init__(self, pBrand, pModel, pColor, pPrice,):
        
         # Declearing variables
        self.brand = pBrand
        self.model = pModel
        self.color = pColor
        self.price = pPrice
        print("Creating an object")
        '''
        *     __str__  is one of the special classes
        *    We use it to return a human readable string that represents the class
        *    We return a string which gives the value of the three instances variable
        *    Which we decleared in __init__
        '''
    def __str__(self):
        return 'Brand = %s, Model = %s, Color = %s, Price = %s' % (self.brand, self.model, self.color, self.price)
        # Declearing  a  normal function except self is important.
        # 
    def SelectColor(self):
        self.color = input('Choose the new color :')
        return self.color
        
    '''
    CalculateTax used to calculate the tax of a vehicle
    '''
    def Tax(self):
        return self.tax
    
    def CalculateTax(self):

        priceWithTax = 1.1*self.price
        
        return self.Total
    
    def VehicleInfo(self):          #class.variable
        print("Company name : %s" % (VehicleImport.company))
        print("Brand        : %s" % (self.brand))
        print("Model        : %s" % (self.model))
        print("Color        : %s" % (self.color))
        print("Price        : %d" % (self.price))
       # print("Tax Rate     : %d" % (priceWithTax)
       # print("Total        : %d" % (self.CalculateTax())
       
       
 ### Creating a object called Honda
print("Vehicle Impund AD\n")
print("Question 1 :")
print("____________\n")
print("Question 1.1 :")
Honda = VehicleImport('Honda', 'Civic', 'White', 15000)
print(VehicleImport.VehicleInfo(Honda))

 ###  Printing the string representation of the vehicle
print("\nQuestion 1.2 :")
print(Honda)

    ### Updating the price for Honda, and return the prince
print("\nQuestion 1.3 :")
Honda.price = 18000
    #  Class.Function.Object
print(VehicleImport.VehicleInfo(Honda))

print("\nQuestion 1.4 :")
Honda.SelectColor()
print(VehicleImport.VehicleInfo(Honda))
