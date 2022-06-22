from random import randint, randrange
from defFunction import isPrime, varScope, addNum

'''
Program :
    Demo - getting to know Python

Author
    @krigjo25

---------------------------------------------------------------------------------------------------------------------------------------------

                                           Chapter 7 - Functions and modules

7.1 What are functions?
  pre written codes which perfomrs a certain task. 

  Can be a part of a class or stand alone
  Some requires data to perform a certain task called Arguments. 
  passes in the function in the parenthese ((required)arg, (required)arg, (1 optional)*arg, (optionals)**kward)

7.2 Defining a own function

    function can be defined by 
        def functionName():
            return

    Def 
        tells the program, the intended code from the next line is a part of the function
    
    return
        tells the program to return an answer from the function, when its executed the function will exit
        if function doesnt need to return a value simply return or return none

    strings, numbers and variable can be declared before assigned to the ()

7.4 Variable Scope
    Variable scope is a conscept for variables defined with-in a function (local variable)
        Can only be acsessed with-in the function

    Variable which is defined outside a function is a global variable
        Can be accsessed every where

    Global variables can be changed with-in the function 

7.4 Default parameters
    a defined function can have default values such as (a,b,c = 5 ) a, b, c, is defined as 5

7.5 Variable Length Argument List

    When we're not sure if there is more than one assignment to pass, there is a * def function(*args) to pass x numbers
        remember to use a loop inside, its passed as a list
    
    formal argument = var
    non-keyworded argument = *var
    keyworded argument = **var

7.6 Importing modules
    Python has a large number of built-in functions. These functions are saved in files known as modules. fuctionfiles.py - modules
    
    import moduleName
        Imports the whole module.
         but modulename.function has to be used
        modules can be imported as keyword (import random as r)

        from module import function. 
            Imports spesific functions
    
    importing modules from another folder.
        import sys
        if 'C:\\MyPythonModules' not in sys.path: sys.path.append('C:\\MyPythonModules')
7.7 Creating our Own Module

    Save the file with .py extentsion, put it in the same folder as the Python file you're importing from

'''

a = 100
num = randint(1,a)
value = isPrime(num)
print("number %3d, is value is %s" % (num, value))


varScope("welcome to Python class")
addNum(1,2,3,4,5,6,7,8,9,10)