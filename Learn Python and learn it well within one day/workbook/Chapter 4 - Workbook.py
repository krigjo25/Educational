'''
Chapter four - Data types
 - Work book
Question 1 :

    Determind the output of the following code, with out running the code
'''
name1 = " Chris" # Declearing variable to Chris
print("1.1 : The user's name is", name1) # Chris gets printed

name2 = "kriss".upper() # Upper function forces the string to uppercase

msg = "1.2 The names %s and %s "%(name1, name2) # Is equal due to retrieveing the same var
print(msg)

'''
Question 2

2.1 Assign the strings 'Python', 'Java' and 'C#' to three var

2.2 Use the var and % operator to generate following strings:

2.2.1 The most popular programming languages are Python, Java and C#

2.2.1 The most popular programming languages are Python, C# and Java.

2.3 Assign the new strings to msg 1 and msg 2 respectively and print te values of msg 1 and msg 2
'''

#2.1
py = "Python"
c = "C#"
java = "Java"

#2.2
msg = " 2.2.1 : The most popular programming languages are %s , %s, %s"%(py, java, c)
print(msg)
msg2 = " 2.2.1 The most popular programming languages are %s , %s, %s"%(py, c, java) 
print(msg2)


'''
Question 3

Determine the output of the following program without running the code:

num = 12

msg = "%d"%(num)

msg = '%4d' %(num)
'''
#3.1
num = 12
msg = " 3.1 : value of num = %d"%(num) # %d(ata
print(msg)

#3.2
msg = '3.2: total value of %4d has not changed' %(num) # %4(total length d(ata) 
print(msg)

'''
Question 4

Determind the output of the following program without running the code:
decnum = 1.72498329745
msg ="5.3f'%(decnum)
print(msg)

msg = "%7.2f"%(decnum)
print(msg)
 '''
# 4.1

decnum = 1.72498329745
msg ="4.1 the value of %5.3f"%(decnum)

# This will print the value of 1.72498
print(msg, "is 1.72498,( max 5 integers .3 decimals) ")
#4.2
msg = "4.2 the value %7.2f"%(decnum)
# This will send the value of 1.72
print(msg, " is 1.72 ( max 7 integers, max 2 decimals")

'''
Question 5

5.1
Assign the values 111 and 13 to two variables


5.2
Devide first Variable by the second, and assign the result to a new variable

5.3
Use the three variables you created and the % operator to generate following strings :
"The result of 111 devided by 13 is 8.538, correct it to 3 decimal places"

5.4
Assign the string to a variable called message and print the value of message.
'''
# 5.1 / 5.2
a,b = 111, 13
c = a/b

print("5.2 The result of %d divided by %d is %d "%(a, b, c))

# 5.3
print("5.3 the result of %d devided by %d is %.3f"%(a, b, c))

'''
Question 6

Determind the output of the following program without running the code

msg = " My name is {} and i am {} years old.".format'("Kristoffer",26)
print(msg) # The result will be : My name is Kristoffer and i am 26 years old.
'''

msg = " My name is {} and i am {} years old.".format("Kristoffer",26)
print("6 ", msg) # The result will be : My name is Kristoffer and i am 26 years old.

'''
Question 7

Determind the output of the followin program without running the code:


msg = "My favorite colors are {} and {}".format("purple", "blue")
msg2 = "I also like {1}, {0} and {2}".format("purple", "blue", "orange")
print(msg, " ", msg2)
'''

msg = "7 My favorite colors are {} and {}".format("purple", "blue")
msg2 = "I also like {1}, {0} and {2}".format("purple", "blue", "orange")

# Those variables will print out the colours which is saved in the arrays
print(msg, " ", msg2) 
'''
Question 8

8.1
Assign the strings "Kriss", "lotte", "aleks", "Linda" to four variables.

8.2
Use the variables and the format() method to generate the following string
" Aleks and Linda is dating, while Lotte is dating someone else. i'll be there for you"

assign the new string to a variable and print the value of the variable
'''

aleks = "Aleks"
linda = "Linda"
lotte = "Lotte"
kriss = "Kriss"
msg = "8.2 : {0:s} & {1:s} are dating. While {2:s} is dating someone else {3:s} be there for {2:s}, when {2:s} need {3:s}".format(aleks, linda, lotte, kriss)
print(msg)

'''
Question 9

Determind the output of the following program without running the code:

msg = "9.1 {:7.2f} and {:d}".format(21.3124, 12)
msg2 = "{1} and {0}".format(213124, 12)
'''
msg = "9.1 {:7.2f} and {:d}".format(21.3124, 12)
msg2 = "9.2 {1} and {0}".format(21.3124, 12)
print (msg)  # This variable will print a value of 21,31, 12
print (msg2) # This variable will print a value of 12, 21.3124

'''
Question 10

10.1
Assign the values 12 and 7 to two variables x and y respectivly then,
Divide x by y and assign the result to a variable

Use the format() method and the variables x,y and result to generate the following strings
" the result of 12 divided by 7 is 1.7143, and correct  to 5 decimal places"

10.2
Assign the  string to a variable  and print the value of the variable
'''

x, y = 12, 7
result = 12 / 7
print(" 10.2 The result of {:d} & {:d} is {:.4f}".format(x, y, result))

'''
Question 11
Assign the value 2.7123 to a variable.

11.1
Cast the variable into an integer and assign it back to the variable.
Print te value of the variable.
'''
decnum = 2.7123
num = int(decnum)
print("11.1 velue of 2.7123 convert into a integer by using int()" , decnum)
'''
Question 12

How do you convert the number 2.12431 into a string
'''
a = 2.12431
b = str(a)
print ("12 by using str() method", b)
'''
Question 13

Assign the string '12' to a variable. Cast the variable into an integer and assign it back
to the variable, print the value
'''
i = '12'
a = int(i)
i = a
print ("13 : the value is ", i)
'''
Question 14

Given that variable = [1,2,3,4,5,6], what is the number at index 1 and idex -2.

Explain why index -6 is invalid
'''
integers = [1,2,3,4,5,6]
print("14.1 This list has its indexes stored with", (integers), "but we get the index from var[]")
print(" here is the second index", integers[1], " Here is the index of -2", integers[-2])
print("14.2 but the index of -6 is", integers[-6])

'''
Question 15

Assign the numbers 10, 11, 12, and 13 to a list
'''
scores = [10, 11, 12, 13]
print("15 Index of our variable [3] and [-1]", scores[3], " and ", scores[-1], " is the same")

'''
Question 16
Determind the output of the following program without running the code

myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
myList1 = myList
myList2 = myList[3:6]
myList3 = myList[:5]
myList4 = myList[2:]
myList5 = myList[1:7:2]
myList6 = myList[ : :3]
print(myList)
print(myList1)
print(myList2)
print(myList3)
print(myList4)
print(myList5)
print(myList6)
'''
myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
myList1 = myList # whole list
myList2 = myList[3:6] # value of index 3-6
myList3 = myList[:5] # to the index of 5
myList4 = myList[2:] # from index of 2
myList5 = myList[1:7:2] # every second value of index 1-7 stepper has the value of 2 from[index:(to) index :7(stepper)]
myList6 = myList[ : :3] # every third index
print("16.1 my whole list includes the integers : ", myList)
print("16.2 Shows only the integers with the index of 3-6", myList2) 
print("16.3 Only integers between 0-5", myList3)
print("16.4 from the second index ", myList4)
print("16.5 every second integer between the index of 1 to index of 7 ", myList5)
print("16.6 shows every third integer value ", myList6)

'''
Question 17


Assign the values 11 - 20 to a list.


Use a slice to select the numbers 13-18 from the variable and assign them to a new list

Use another slice to select the numbers 13, 16, 19 from the variable, assign them to a new variable

print both variables
'''
listItem = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
listItem[2:7]
print("17. The integers is now %d", listItem[2:8])
print("17.1 There is only three integers taken from the list", listItem[2:9:3])
'''
Question 18

Create a list, with no initial values.

18.1 :
add numbers 5, 9, 11, 12 to the list and print the list
'''
listIntegers = []
listIntegers.append(5)
listIntegers.append(9)
listIntegers.append(11)
listIntegers.append(12)
print("18.1 These values were added", listIntegers)


'''
Question 19
Assign the numbers 1, 2, 4, 5 to a list

19.2
Change the third number to 10 and print the value
'''
listIntegers = [1, 2, 3, 4, 5]
print("19.1 ", listIntegers)
listIntegers[2] = 10
print("19.2", listIntegers)
'''
Question 20

Assign the letters 'A', 'B', 'C', 'D' and 'E' to a list.
Remove 'A' and 'C'from the list and print the list.
Hint: It is easier to remove 'C' first.

Why do you think that is so?
'''
li = ['A', 'B', 'C', 'D']
print("20.1 ", li)
del li[2] # It's easier to remove index of 2 first than 0, due to the index changes if index 0 is removed
del li[0]
print("22.2", li)

'''
Question 21

Assign the strings 'Sun', 'Mon', 'Tues', 'Wed', 'Thurs', 'Fri' and 'Sat' to a tuple
called daysOfWeek.
 Assign the third element in daysOfWeek to a variable called myDay and print the value
 of myDay.
'''
daysOW = ('Sun', 'Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat')
mDay = daysOW[5]
print("21 ", mDay)

'''
 Question 22
 What is wrong with the following dictionary?
 nameAgeDict = {'John':12, 'Matthew':15, 'Aaron':13, 'John':14, 'Melvin':10}
'''
# Used same Dictionary key twice, it will neither overwrite, or print it
nameAgeDict = {'John':12, 'Matthew':15, 'Aaron':13, 'John':14, 'Melvin':10}
print(nameAgeDict)
'''
 Question 23

Determine the output of the following program without running the code:
dict1 = {'Aaron': 11, 'Betty': 5, 0: 'Zero', 3.9: 'Three'}
print(dict1['Aaron'])
print(dict1[0])
print(dict1[3.9]) # Printing "Three"
dict1['Aaron'] = 12 print(dict1)
del dict1['Betty']
print(dict1)
'''
dict1 = {'Aaron': 11, 'Betty': 5, 0: 'Zero', 3.9: 'Three'}
print(dict1['Aaron']) # Accsessing Aaron's index value
print(dict1[0]) # same as above + name
print(dict1[3.9]) # Printing "Three"
dict1['Aaron'] = 12, print(dict1) #nothing
del dict1['Betty'] # Deletes only the Dictionary key,
print(dict1)

'''
Question 24

The statement below shows one way of declaring and initializing a dictionary called dict1.
dict1 = {'One':1, 'Two':2, 'Three':3, 'Four':4, 'Five':5}

    (a) Rewrite the statement above using the dict() method to declare and initialize dict1.
    (b) Print the item with key = 'Four'.
    (c) Modify the item with key = 'Three'. Change it from 3 to 3.1.
    (d) Delete the item with key = 'Two'.
    (e) Use the print() function to print dict1.
'''
myD = dict(One = 1, Two = 2, Three = 3, Four = 4, Five = 5)
print ("24.1 ", myD)

print("24.2 ", myD['Four'])

myD['Three'] = 3.1
print("24.3 ", myD)
del myD['Two']
print("24.4 / 24.5 ", myD)

'''
Question 25

Create a dictionary that maps the following countries to their respective capitals.
The capitals are indicated in parenthesis beside the country names below.
USA (Washington, D.C.)
United Kingdom (London)
China (Beijing)
Japan (Tokyo)
France (Paris)

25. 1  The country name should serve as the key for accessing the capital.
Next, print the dictionary.

25.2 Delete the third country from the dictionary and print it again.

25.3 Add the following two countries to the dictionary and print it again.
Germany (Berlin)
Malaysia (Kuala Lumpur)
'''
myC = {'China':'Bijing', 'France':'Paris', 'Japan':'Tokyo', 'UK':'London', 'USA':'Washington D.C'}
print("25.1 ", myC)

del myC['Japan']
print("25.2", myC)

myC['Germany'] = 'Berlin'
myC['Malaysia'] = 'Kuala, Lumpur'
print ("25.3", myC)





