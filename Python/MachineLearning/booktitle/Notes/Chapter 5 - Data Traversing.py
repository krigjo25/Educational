# -*- coding: utf-8 -*-
"""
Chapter 5 Data Traversing

Created on Thu Apr 22 03:01:02 2021

@author: krigjo25

In this chapter we will navigate and traverse through the data structures. 3 ways
    If, else statement
        If else statements are conditional structures, they're common presence in oop-languages
        They make use of Boolean operators as instroduced in chapter 3 Data types
        (>,<, ==)
       
        wiz = 'Merlin'
        power = False
        theDarkOne = False

        # If statements
        if wiz == 'Sauroman':
            print('Oh no')
   
        elif wiz == 'TheDarkOne':
            print("Thats even worse, Help !")
    
        elif wiz == 'Merlin' and power == True:
            print('We\'re saved !')
        else:
            print("Apocalypse")
    
            
        Boolan And fuction checking if both is True or False
        Since both conditions in elif nr 2 ain't fullfilled, it get skipped
        
        
    Loops
        For loops and while loops are also common in oopl
        For loops is used to traverse data structures based on specific conditions.
        
        l1 = [1, 2, 3, 4, 5]
        for i.list in enumerate(l1):
            l1[i] = list + i
            print(l1)
            
     Other example of a loop is while liips works for traversing data structures 
     where the data size is unkown, and you'd like to traverse untill a spesific traversion is met

        i = 0
        metals = ['Silver', 'Gold', 'Copper', 'Iron', 'bronze', 'Diamond']

        while metals[i] != 'Diamond':
            print('hop ' + str(i))
            i = i+1
        print('Diamond Found')
        
        In the code above, we're searching for a spesific array, but the ammount of hops is unkown
        So we set the index to 0 and let the program keep going untill the metal is found
        after x hops we find the metal we're looking for.
        
    Functions
    
    In programming languages we can define our own functions, def DefName():
        Custom function can be defined as:
            
            # Defining the function multiple
            def Multiple(x, li):
                
                for i, list in enumerate(l1):
                    l1[i] = list + i
                    print(l1)
                    
            # Trying the function
                # Variables
            li = [13, 15, 17, 19]
            
            multiple(4,li)
            print(li)
"""
# Creating a variable called Merlin
wiz = 'Merlin'
power = False
theDarkOne = False

# If statements
if wiz == 'Sauroman':
   print('Oh no')
   
elif wiz == 'TheDarkOne':
    print("Thats even worse, Help !")
    
elif wiz == 'Merlin' and power == True:
    print('We\'re saved !')
else:
    print("Apocalypse")
    
    
# Loops
    # Odd numbered list
l1 = [1, 2, 3, 4, 5]
       # Converts them to even numbers, can be converted as list are mutable
for i, list in enumerate(l1):
    l1[i] = list + i
    print(l1)

s1 = {
      'one',
      'two',
      'three',
      'four'}
for i in s1:
    print(i + ' Indians')

    # While loops
i = 0
metals = ['Silver', 'Gold', 'Copper', 'Iron', 'bronze', 'Diamond']

while metals[i] != 'Diamond':
    print('hop ' + str(i))
    i = i+1
print('Diamond Found')

# Functions 

 # Defining the custom function
            # Defining the function multiple
def Multiple(x, li):
    
    for i, list in enumerate(l1):
        l1[i] = list * x
        print(l1)              
    # Trying the function
        #Variables

li = [13, 15, 17, 19]
print(li)     
Multiple(4,li)
print(li)