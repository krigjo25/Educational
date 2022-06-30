## Initiating a class object
class Polyform:

    #   Initializing class variables
    company = 'Polyform Norway'

    def __init__(self, pos, name, salary):

            #   initializing Instances variables
            self.pos = pos
            self.name = name
            self.salary = salary

            return

    def PrintInfo(self):return print(f'at {Polyform.company} {self.name} has the position as {self.pos}, with salary at {self.salary}$')

#   Initiating a new class object
class ProStaff:

    #   Creating a Initializer
    def __init__(self, pos, name, salary):

        self._pos = pos
        self.name = name
        self.salary = salary

        return print('Creating Prostaff Object')

    def __str__(self):

        return f'Position {self._pos}, Name {self.name}, Salary {self.salary}'

    #   Overriding the __add__ method #10.4
    def __add__(self, other):
        return self.salary + other.salary
    # 9.4  Using property decorator
    @property

    #   Getter method
    def Pos(self):

        print('Getter method')

        return self._pos

    #9.4   Setter method
    @Pos.setter
    def Pos(self, value):

        if value == 'Mananger' or value == 'Basic':
            self._pos = value

        else:
            print('Position does not exists. No changes made.')

        return

    #   Creating a method called CalculateSalary
    def CalculateSalary(self):

        ''' CalculateSalary
            Calculates the Salary for the employees.
        '''
        #   Initializing variables
        msg = f'\nEnter number of hours worked for {self.name}'
        msg1 = f'\nEnter the h/rate for {self.name}'

        #   Declear inputs
        h = input(msg)
        hr = input(msg1)

        #   Converting from string into integer
        h = int(h)
        hr = int(hr)

        self.salary = h*hr

        return self.salary

#   Initiating a new child class object
class Junior(ProStaff):

    def __init__(self, name, salary):
        super(Junior, self).__init__('Junior', name, salary)

        return

#   Initiating a new child class object
class Management(ProStaff):

    def __init__(self, name, salary, allowance, bonus):
        super(Management, self).__init__('Mananger', name, salary)

        #   Initializing instances
        self.bonus = bonus
        self.allowance = allowance,
        return

    #   Overriding the method in the parent class
    def CalculateSalary(self):

        #   Titles
        jr = super().CalculateSalary()
        self.salary = jr + self.allowance

        return self.salary

    def CalculateBonus(self):

        #   Prompting the user to enter the performance grade for the management staff
        a = f'Enter performance grade for {self.name}'
        grade = input(a)

        #   Assigning bonus value based on grade
        if (grade == 'A'):
            self.bonus = 10000
        else:
            self.bonus = 0

        return self.bonus

class ParentClass:

    def __init__(self):

        #   Initiating a new instance
        self.a = 1

        return print('Parent Class Object Created')

    def SomeMethod(self):
        return print('Hello World')

class ChildClass(ParentClass):

    def __init__(self):
        return print('Child Class Object Created')