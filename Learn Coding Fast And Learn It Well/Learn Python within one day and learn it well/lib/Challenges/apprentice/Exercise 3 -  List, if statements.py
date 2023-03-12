'''
Exercise 3.1 
Take a list, say for example this one:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5.

Extras:

Exercise 3.1
Instead of printing the elements one by one, make a new list that has all the elements less than 5
from this list in it and print out this new list.
Write this in one line of Python.

Exercise 3.2
Ask the user for a number and return a list that contains only elements from the original list a that
are smaller than that number given by the user.
Task one :

x = [ ]
print("  Task 1.0 : In this program you'll be able to type up to 10 inputs (positive or negative integer) \n you may only choose one each input")
for i in range(1, 11): # for variabelen i i range(1-10) Teller ipt 10 ganger
    ipt = int(input( '%s Choose an integer : ' % ( i )))
    x.append(ipt) # Legger ipt verdien i listen
    if i == 10: # Hvis variabelen er lik 10 
        for p in x: # Får variablene ifra listen  til å bli heltall
            if p < 5:
                print("Task 1.0 : \n", p)
        #Task 1.2
'''
a = [1, -1, 2, 5.9, 76, 3.9, 77, 99]
o = [ ]
x = [ ]
print("  Task 1.2 : In this program you'll be able to type up to 10 inputs (positive or negative integer) \n you may only choose one each input")
for i in range(1, 11): # for variabelen i i range(1-10) Teller ipt 10 ganger
    ipt = int(input( '%s Choose an integer : ' % ( i )))
    x.append(ipt) # Legger ipt verdien i listen
    if i == 10: # Hvis variabelen er lik 10 
        for p in x: # Får variablene ifra listen  til å bli heltall
            if p < 5: # Tallene som er mindre enn 5
                o.append(p)  
                print("Task 1.2: ", o)

#-----------------------------------

'''
+If statesment :

Om i er mindre enn, mer enn eller er lik =  start oppgaven.

For loop:

for i in pets:
Fordi i i variabelen, overfør til i og print ut en og en

While I er mindre enn, mer enn eller er lik var gjør oppgaven.
'''
