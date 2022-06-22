'''
Program :
    Demo - getting to know Python

Author
    @krigjo25

---------------------------------------------------------------------------------------------------------------------------------------------

                                            Chapter 9 - Object Oriented Programming (OOP) Part 1 ( page 74)

9.1 What is OOP? 
     OOp Is like a book where the cover is the oop, and pages methods, 
    it is an approach to programming that breaks a programming problem into objects that interact with each other.
    Objects are created from templates known as classes. You can think of a class as the blueprint of a building. 
    An object is the actual “building” that we build based on the blueprint. To understand how object-oriented programming works, 
    let’s start by coding a simple class together.

9.2 Writing our own class

    Class keyword followed by the name of the class.

    - Comon practice PascalCasing (CamelCase)
    A class consist of variables and functions. We've learned so far :
        - Variables storing data
        - Functions code blocks to perform a certain tasks for us. Function with-in a class is more formaly called for methods.

    An instializer is called whenever an object of the class is created. 

    self keyword refers to an instance itself.

9.3 Instaniating an Object

    How to use the class
        Calling the class
            ceo = ProStaff('Jane Doe', 'Prostaff CEO', 1000000)
        
        Accsessing instance variables / methods
            ceo.name,
            ceo.pos,
            ceo.salary
            ceo.calculateSalary()
        altering instance variables
            ceo.name, ceo.pos, ceo.salary = 'Jake Doe', 'Python Developer', 2000
        
9.4 Properties

    To prevent error, such as wrongly altering positions or salary
    we use properties. They provide us with a way to check the values 
    of the changes which we want to make before allowing the changes occour
    
    @property 
        known as a decorator
        allows us to alter the functionallity of the method which follows by using ceo.pos
    
    @method.setter
        When users tries to update the value of _pos  by using
        ceo.pos = 'Manager' it should use the pos() method to update the value. e.g(ceo.pos = value)
        if the value is neither 'Manager' or 'Ceo' the value will not be updated 
        after declaring those two properties, you no longer accsess directly to the value


    - adding single underscore in front of a variable notifies other developer to not accsess that variable directly unless,
        They have a compelling reason to.

    - adding two underscores, just means no touchy
9.5 Name Mangling
'''
class ProStaff:
    # Instializer
    '''             Instance variables
                        pName, 
                        pPos, 
                        pSalary

                    Method / function            
                        __init__,
                        __str__,
                    calculateSalary                    
                                            '''
    def __init__(self, pName,pPos, pSalary):

        self._pos = pPos
        self.name = pName
        self.salary = pSalary

        print('Prostaff employe Created')

        # Readable string
    def __str__(self):
        return '\nEmploye Info:\nName = %s,\nPosition = %s,\n139Salary = %s\n' % (self.name, self._pos, self.salary)

    @property
    def pos(self):
        print('Getter method')
        return self._pos

    @pos.setter
    def pos(self, value):
        if value == 'Ceo' or value == 'Manager':
            self._pos = value
        else :
            print('Invalid Position')

    
    def calculateSalary(self):
        prmpt = '\nEnter number of hours worked for %s:' %(self.name)
        prompt = '\nEnter the hourly rate for %s:' %(self.name)

        hours, rate = input(prmpt), input(prompt)

        self.salary = int(hours)*int(rate)
        
        return self.salary


'''
Calling the Class
'''   
ceo = ProStaff('Jane Doe', 'Prostaff Ceo', 1000000)
ceo.calculateSalary()


print(ceo)
ceo.pos = 'CEO'
print(ceo.pos, ceo.name, ceo.salary)