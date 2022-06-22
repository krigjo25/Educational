'''
Question 3 :

* For the code below, add a property called bonus
  for the instance variable_bonus.

 class HumanResource:
    def __init__(self, pName, pSalary, pBonus):
        self.name = pName
        self.salary = pSalary
        self.bonus = pBonus

    def __str__(self):
        return 'Name : %s\nSalary : %.2f\n.Bonus =%.2f'&(self.name, self.salary, self.bonus)
 The getter method of the property simply returns the value of _bonus.


The setter method, on the other hand, allow us to
set the value of _bonus. If we try to set it to a 
negative value, the setter method should display
the message :

"We regret to inform you, the bonus cannot be a
negative value"

** Outside the class, instantitate a HumanResource
object called "cheifObs" with the followin values.


name : 'Kelly'
salary : 7150000
_bonus : 0



* Use the bonus property to set _bonus to -20 for
cheifOps. Verify that you get the error message.



* Next, use the bonus property to change _bonus
to 50000. Then use the getter method of the 
property to verify that  _bonus is set correctly

'''
class HumanResource:
    def __init__(self, pName, pSalary, pBonus):
        self.name = pName
        self.salary = pSalary
        self.bonus = pBonus
        print("Employee ", self.name, " Were created")

    def __str__(self):
        return'Employee Name:   %s \nSalary: %.2f \nBonus: %.2f\n' % (self.name, self.salary, self.bonus)

    def SetBonus(self, x):
        if x >= 0:
            self.bonus = x
            return self.bonus
        else:
            print("Bonus were not changed\n")
    
    def GetBonus(self):
        if self.bonus >= 0:
            return self.bonus
        else:
            print("Bonus can not be less than 0.")
            
    def CalculateSalary(self):
        bonus = self.bonus
        salary = self.salary
        self.salary = bonus*salary
        
        return self.salary
    
# Question 3.1 Create a class named cheifOps
# Variable = class
cheifOps = HumanResource('Kelly', 7150000, 0)

# Question 3.2 Print the value of the class HumanResource (__str__)
print(cheifOps)

#Question 3.3 Set the bonus to -20
cheifOps.SetBonus(20)
cheifOps.GetBonus()
# Calculates new Salary
cheifOps.CalculateSalary()

# Updated Info
print(cheifOps)