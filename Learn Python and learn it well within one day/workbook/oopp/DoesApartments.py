
'''
Question 2 :

Write a Class called Room that has four instance variables, size, view, type and basicRates.

Whitin the class, you need to have the __init and __str__ methods.

Question 2.1 :

Next write an instance methood called calculateRates() within the Room class.

The CalculateRate() methhod has a parameter (in addition to self) called day.
Based on the value of day, the method multiplies basicRates by a certain factor.


If day equals 'Weekends', it multiplies basicRates by 1.5
If day equals 'Public Holidays', it multiplies it by 2.
If day equals 'Christmas'it multiplies it by 2.5.
For any other values of day, it multiplies it by 1.
After multiplying, the method returns the result.

*  Next, outside the class, instantiate a Room object called room1
with size = 132, view = 'City', type = 'Duble' and basicRates = 120 and print a string
representation of room1.

* Use room1 to call the calculateRates() method, using 'Public Holidays' as the argument.
Assign the result to a variable called newRates and print the value of newRates.
'''
class DoesApartments:
    
    def __init__(self, pSize, pView, pType, pRates):
        self.size = pSize
        self.view = pView
        self.type = pType
        self.rates = pRates

    def __str__(self):
        return 'Type of Apartment %s. \nThe Size : %s kvadratmeter. \nThe beautiful view of the %s.\nRates at %d$\n' % (self.type, self.size, self.view, self.rates)

    def CalcRates(self, day):

        weekEnd = 'Weekend'
        pHolidays = 'Public Holidays'
        xmas = 'Christmas'
        
        if day == weekEnd:
            
           return 1.5*self.rates
            
        elif day == 'Public Holidays':
            return 2*self.rates
            
            
        elif day == xmas:
            return 2.5*self.rates
    
        else:
            1*self.rates
            
    def DoesInfo(self):
        currency = '$'
    
        print("Information about the selected apartment :\n")
        print("Apartment type : %s." % (self.type))
        print("View of the %s" % (self.view))
        print("Size : %s m2" % (self.size))
        print("Regular rates : %d %s " % (self.rates,currency))

print("Question 2:")
print("___________\n")
print("Jhon & Jane DoesApartment \n")
lApartment = DoesApartments('200', 'County','Luxe', 1200)
print(lApartment)
DoesApartments.DoesInfo(lApartment)
DoesApartments.CalcRates(lApartment, 'Public Holidays')
