'''
Program :
    Demo - getting to know Python

Author
    @krigjo25

---------------------------------------------------------------------------------------------------------------------------------------------

                                                    Chapter 4 - Data types in python

 Basic data types integer, float and string
advanced data types : list, tuple and dictionary

4.1 Integers
    Numbers with out decimal places eg. -5 - 5
    declaration variableName = initial value
    f.eks mobile numbers equals integers.

4.2 Float
    Numbers with decimal parts as 3.14 etc.
    same declaration as integers

4.3 Strings
    strings equals text ('', "")

4.4 Type Casting in Python
    Converting string into integers, integers into string etc
    bultin function : int(), str(),float()
    int("1") converts into 1, but int("1.2") doesnt work neither does int("str")

4.5 List
    Refers to a collection of dataq which are normally related. They are ordered
    e.g 
        uAlias = ['jhon', 'Jake', 'Timmb']
        uAge = [21,23,24,51,53]

    Can be accsessed using index 
    e.g 
    uAlias[0]

    Notation uAlias[start:end] is known as slice, includes a third number known as stepper uAlias[start:end:Stepper]
    Slices has a default value whihch is zero

    bult-in functions :
        .append() - Add one more to the list,
        del list[index] - remove one from the list.

4.6 Tuples
    Declaring a tuple : tupleName = ()
    ex :
        monthsOfYear = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")

    Same as list, beside it can NOT be altered when the tuple is set.

4.7 Dictonary
        Dictionary : dictionaryName {key:data} / dict(key:data)
                                        - keys are requered to accsess the information, keys can be strings, integers

    A collection of related data PAIRS
    Set same as dicitonary besides the key, and they're not ordered.
    acsessing a dictonary dictName[key]
    adding values to a dictonary dictName['key'] = value
    removing values from a dictonary del dictName[key]

'''

num = 46652938
print("4.1  integers %s" % (num))

pi = 3.14
print("4.2 float %4.2f" % (pi))


num = 'Hello Python !'
ok = num.upper()
lol = ok.lower()
brand, exr = 'Android', 1.2345
msg = "4.3 Strings\n %s \n %s \n %s \n %s, %4.2f" % (num, ok, lol, brand, exr)
print(msg)

uAlias = ['jhon', 'Jake', 'Timmb']
uAge = [21,23,24,51,53]

print("4.4 Printing the lists : \n", uAlias, uAge)
print("4.4 Printing an index of th list : \n", uAlias[2], ", ", uAge[0])

uAlias.append('Japalano')
print("4.4 Printing a sliced list : \n", uAlias[0:1], ", ", uAge[2:4])
print("4.4 Printing a sliced list with stepper : \n", uAlias[0:3:2], ", ", uAge[0:3:2])

del uAlias[2]
print("4.4 Printing a sliced list : \n", uAlias[0:1], ", ", uAge[2:4])
print("4.4 Printing a sliced list with stepper : \n", uAlias[0:3:2], ", ", uAge[0:3:2])

uAlias = {  0:23,
            1:24,
            2:25,
            3:26,
            4:21,
            5:12}


