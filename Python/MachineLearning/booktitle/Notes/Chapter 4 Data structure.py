# -*- coding: utf-8 -*-
"""
Chapter 4 - Data structures

Created on Thu Apr 22 02:07:06 2021

@author: krigjo25
"""
'''
Data Structures

    Tuples
        Ordered sequences of data, () seperated by , e.g
            (1, 'two', 3.5 false)
        Tuples can be nested like : tupleName[0:0] (3,4) 3 tupleName[0:1] (3,4) 4
        
    List
        Represented as seperated by [] e.g
        newList = [1, 'Two', 3.5 false]
        
        Basicly just like tuples
        
    Dictionaries,
        Main differences between Dictonaries, Tuples and Lists. Dictionary seperates labeled
        Data with , and {} e.g.
        {'President': ' Abraham Lincon', 'City':'Warshinton D.C'}
        
        Index or keys cannot be changed, but labels can be
        
    Sets
        Are not ordered ( No indexes ). Contains unique elements. Seperated by , and {}
        (s1 = {1,'two', 3.5, 4.6, false})
        
        Possiblity to add and remove a value, using mathematical functions.
        To view common elements use & function
        s2{'Hey', 4.6, 1, 'i', 'new'}
        
    Custom Object
    While the others is built-in data. Custom Object (OOP) is defined classes in python
    
    e.g.
    # Defining the class
        class Human ( object ):
            
                # Initalizing the custom class
                def __init__(self, pName, pAge, pWeight, pHeight, pBodyfat):
                    self.name = pName
                    self.age = pAge
                    self.weight = pWeight
                    self.height = pHeight
                    self.massindex = pBodyfat
                    print('Human %s Created' % (self.name))
            
                # Readable string
                def __str__(self):
                    return '\n Profile information of : %s,\nAge : %d years old.\nWeight : %f2.1 kg,\n Height %f2.1 cm, \nbody mass index %f2.1\n ' % (self.name, self.age, self.weight, self.height, self.massindex)

        The 'Self' is an instance of an object
    
'''

# Dictionary example
d1 ={
     'President':'Abraham Lincon',
     'city':'Warshington D.C'
     }

d1['President'] = 'George Clinton'
print(d1)

# Sets example
s1 = {
      1,
      'two',
      3.5,
      4.6,
      4.6, # Duplicate gets removed
      False}

s2 = {
      'Hey',
      4.6, 
      1,
      'i',
      'new'}
s1.add('Twinkle, twinkle') # Adding a string to the set
s1.remove(False) # Removing a string from the set
print (s1)
print (s1&s2)

union = s1.union(s2) # Combine s1 with s2 // Doesnt send duplicates
print(union)

# Custom Object | Object Orientated Programming
# Defining the class name
class Human ( object ):
    # Initalizing the custom class
        def __init__(self, pName, pAge, pWeight, pHeight, pBodyfat):
            self.name = pName
            self.age = pAge
            self.weight = pWeight
            self.height = pHeight
            self.massindex = pBodyfat
            print('Human %s Created' % (self.name))
            
            # Readable string
        def __str__(self):
            return '\n Profile information of : %s,\nAge : %d years old.\nWeight : %f2.1 kg,\n Height %f2.1 cm, \nbody mass index %f2.1\n ' % (self.name, self.age, self.weight, self.height, self.massindex)
        
        # Converts kilo to ponds
        def KiloToPounds(self):
            lbs = 2.20462262185
            kg = float(self.weight)
            self.weight = kg * lbs
            return self.weight
        
nH = Human('Jhon Doe', 27, 70, 183, 20)

# Printing the human out
print(nH)
print(nH.KiloToPounds())
print(nH)