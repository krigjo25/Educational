'''
Program :
    Demo - getting to know Python

Author
    @krigjo25

---------------------------------------------------------------------------------------------------------------------------------------------

                                            Chapter 3 - World of Variables and Operators

3.1 What are variables
    Variables are names given to data

3.2   Naming a variable
variables can only contain letters between a-z, A-Z, numbers and underscore. 
First Character can NOT be numberic.

variables can not be reserved words

3.3 The Assignment Operator

 "=" means assign to, not like matimatic

here we assign the value, at right to the variable, left
 userAge = 0 

3.4 basic operators +, -, /, //, %, **

3.5 More Assignment Operators
+=,-= and *=

'''
# Assigning zero to a name called userAge
userAge = 0 

# Defining multiple variables
userAge, userName = 30, 'Peter'

x,y = 5,10
x=y
print ("x = %d,\n y = %d." % ( x,y ))

x,y = 5,10
y=x
print ("x = %d,\n y = %d." % ( x,y ))

a,b = 5,2

c = a + b
d = a - b
e = a*b
f = a/b
g = a//b
h = a%b
i = a**b
print ("a = %d, b = %d, \n c pluss +: = %d, d substraction -: = %d,\n e multiplication*: = %d, Devision /: = %d,\n g// = %d,\n h modules : = %d. \n Exponent**: %d" % ( a, b, c, d, e, f, g, h, i))


x,y = 5,10
x += y
y += 2
print ("\n 3.3 += assignment : \nx = %d, y = %d." % ( x,y ))