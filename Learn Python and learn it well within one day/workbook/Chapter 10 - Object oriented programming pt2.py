'''
Chapter 10 Object Oriented Programming Part 2

Question 10.1

Create a file called shape.py and save it onto your desktop. Add the following code
to the file:

class Shape:
    def __init__(self, pType, pArea):
        self.type = pType
        self.area = pArea

    def __str__(self):
    return '%s of area, %4.2f unit square' %(self.type, self.area)

class Square(Shape):
    def __init__(self, pLength)
    super().__init__('Square',0)
    self.length = pLength
    self.area = self.length * self.length

The code above consist of two classes - Shape and Square.

Square is a subclass that inherits from Shape. This subclass only has one instance
__init__, with two parameters self and Length.

Within the method, we first call the __init__ method from the parent  class
(using the super() function), passing in 'Square and 0 as arguments.

These arguments are used to initialized the instance variables type and area in the parent
class, which the subclass inherits.

Next we assign the parameter pLength to a new instance variable called length. In addition,
we calculate the area of a square and use it to update the value of the inherited instance
variable area.

( Note :
The area of a square is given by the square of its length).

Study the code above and make sure you fully understand it.


Next, we need to add two more subclasses, Triangle and Circle, to shape.py.
Both subclasses have one method: __init__.

You need to decide on the appropriate parameter(s) for these methods.

Both __init__ methods should call the __init__ method in the parent class and pass in
appropriate values for the inherited instance variable type and area.

In addition, they should have their own instance variable and contain a statement for
updating the value of the inherited instance variable area.

Try modifying the Square subclass your self to code the Triange and Circle subclasses.


Hint :

    Triangle is defined by its base and height and its area is given by the mathematical
    formula :  0.5*base*height.

    A Circle is defined by its radius and its area is given by mathematical formula :
        Pi*r*r

    pi is a constant represented as math.pi in the math module. You need to import the math
    module to get the value of pi.

Question 10.2

In this question, we shall modify the Shape class in Question 1 by adding one more method to
it - the __add__ method.

This method has two parameters, self and other, and overrides the + operator. instead of
performing basic addition, the + operator should return the sum of the areas of two Shape
Instances. In other words, if one instance has an area of 11.1 and another has an area of
7.15, the __add__ method should return the value of 18.24.

Add the __add__ method to the Shape class in shape.py.

Next, use the print() function in shapemain.py to verify that sq + c gives you the sum of
areas of sq and c.

Question 10.3

In this question, we'll tryto use the __add__ method in Question 10.2 to find the sum of the
areas of sq, c and t.

Try doing prin(sq + c + t) in shapemain. What happends? You get an error, right?
This is because the + operator is trying to do sq + c first, before adding the result to t.


However, notice that sq + c gives us a numerical value, whihc is the result of sq.area +
c.area.

When we try to add sq + to t, we get an error because the + operator is unable to add sq +
c (Which is a float) to t (Which is a Triangle instance.

If you study the __add__ method, you'll see that the + operator expects both the arguments
( for the self and other parameters ) to be instances of the shape class
( Or instances of subclasses of the Shape class ).

To overcome this, we need to chang the __add__ method. Instead of returning a numerical
result, we need it to return a Shape instance so that we can pass this result to the +
operator again so do futher additions.

To do that, we'll change the return self.area + other.area statement in the _add__ method
to return Shape('New Shape', self.area + other.area)

Next in shapemain try doing print(sq + c + t) again and verify that you get a new shape
instance (type ='New Shape') whose area is the sum of the areas of sq, r, and t.
    
'''
from oopp_two.shape import Circle as C
from oopp_two.shape import Triangle as T
from oopp_two.shape import Square as S

c = C(11.1)
s = S(7.5)
t = T(3.2, 5)

print ("Question 10.1 : \n", c, "\n", s, "\n", t, "\n")

print ("Question 10.2 : \n Total area : ", c + s, " \n")

print ("Question 10.3 : \n", c + s + t)

'''
Question 10.4

Create a class called Student.

The class has 4 instance variable: name, id, course_enrolled and annual_fees.
Within the class, we need to have an __init__method to initialize the 4 instance variables.
We also need to have a __str__ method.

Code the class your self.

Next we inherit three subclasses from Student. The first subclass is ArtStudent.
It has a additional instance variable called pProjectGrade

The second subclass is CommerenceStudent. It has an additional variable called
internship_company.

The third subclass is TechStudent. It has two additional instance variables called
internship_company and project_grade.

Least but not least, we need to add the __It__ and __gt__ methods to our parent class.
These are special methods in Python that allow us to make comparison.

LT stands for "less than" while GT stands for "greater than". They override the < and >
operators respectively.

Add these two methods to the Student class so that they allow us to compar the annual fees
(sstored in the instance variable annual_fees) of two instances and return True or False
accordingly. For instance, if we have the follwoing code :


student1 = Student('jim', 'A19001', 'Psychology', 12000, 'In Progress')

student2 = CommerceStuden('Ben', 'C19011', 'Marketing', 15000, 'Cool Mart)

student1 > student2 should give us False as the annual_fees of student1 is lower than that
of student2

In contrast, student1 < student2 should give us True.

Once that is done, save the file as student.py on your desktop.
Next, create another file called ch10q4.py on your desktop and import the classes in student.py

Instantiate three instances with the following information and print a string representation
of each instances :



'''
from oopp_two.student import ArtStudent
from oopp_two.student import ComStudent
from oopp_two.student import TechStudent

st1 = ArtStudent('Jhon Doe', 'A19001', 'Psychology', 12000, 'in Progress')
st2 = ComStudent('Jane Doe', 'C19011', 'Marketing', 15000, ' Cool Mart')
st3 = TechStudent('Martin Doe', 'B29011', 'Python', 10000,' Prostaff', 'Calculating.. ' )
print(st1, "\n", st2, "\n", st3, "\n")
print(st1 < st2)

