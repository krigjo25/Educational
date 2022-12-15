'''
Question 6 :

* Write a class called Student that has two 
instance variables : name and marks, and one class
variable, passingMark, Assign 50 to passingMark.

Within the class, you need to code the __init__
and __str__ methods.

** Next, write an instance method called 
passOrFail() within the Student class. This method
returns the string "Pass" if marks is greater than
or equal to passingMark or "Fail" if marks is lower
than passingMark.

***	Outside the class, instantiate a Student object
called Student1 with name = 'Jhon' and marks = 52
and use it to call the passOrFail() method. Assign
the results to a variable called status1 and print
the value of status1.

*** Instantiate another Student object called student2
with name = Jenny' and marks = 69 and use it to call
the PassOrFail() method. Assign the result to a
variable called status2 and print the value of 
status2.

***** Update the value of passingMark to 60 for all
Instances of the Student class and call the 
passOrFail() method for student1 and student2 again.
Assign the result to status1 and status2 
respectively and print the two values
'''

class Student(self, pName,):
    def __init__():
        self.name = pName
        self.mark = pMarks
		
    def __str__():
        return 'Student : %s\n score : %d/100' % (self.name, self.mark)	

    def PassOrFail():
        marks = self.mark
        if mark >= 50:
        	print("You\'ve passed")
        else:
            print("You did not pass")

student = Student('Jhon Doe', 52)
student = Student('Jhon Doe', 52)
student.PassOrFail()
