'''
Program :
    Demo - getting to know Python

Author
    @krigjo25

---------------------------------------------------------------------------------------------------------------------------------------------

                                           Chapter 5 - Making Choices and Decisions
 - Looking at the control flow  such as if, for, while, try and except

6.1 Conditon statements
    Comparison operators :
        not equal !=
        Greater than >
        Smaller than <
        Greater than or equal to >=
        Smaller than or equal to <=

6.2 If Statements
        Allows the program to evaluate if a certan condition is met

    If conditon 1 is met: 
        do A

        elif condition is met:
        do B
    else:
        do D

6.3 Inline if statement
    Simple form of an if statement, more convinient if there is only a simple tast to perform.
    Do task a if condition is true else do Task B

6.4 For loop
    Executes statements untill there is nothing else to execute execute

    Can be used with :
        list, tuples and dictionaries
    
    Bultin functions
        enumerate(), 
        .items(),
        range()  

    Tip
        Unless otherwise stated, it starts from zero.

    looping through a variable text looping through a sequence of text

6.5 While loop
    While the condition is true do A

6.6 Break
    Exit the loop when condtion a is met.
    if not used the statement will continue untill another statement is met

6.7 Continue
    Opposite of break, but skips selected variable when a certain condition is met

6.8 Try, except
    Controls how a program proceeds when an error occours.
'''
uName = input(' Please insert a name : ')
uInput = input('Greetings %s, enter an integer:' % (uName)) 

num = 1 if uInput == "1"  else 13 

if uInput == "1":
    print (" 6.2 If Statements :\n Hello %s, you inserted a value of %s" %(uName, num))

elif uInput == "2":
    print (" 6.2 Elif Statements :\n Hello %s, you inserted a value of %s" %(uName, num))
else:
    print (" 6.2 Else Statements :\n Hello %s, you inserted a value of %s" %(uName, num))

# For loop
myList= ["A","B","C", 'D']

myd = {0:'krigjo25',
        1:'demo'}

myt = (1,2,3, 'apple')

msg = "Greetings Python world !"

l = 5

for i in myList:
    print("6.4 For loop, list \n %s \n "% (i))

    for i, j in enumerate(myList):
        print("number : %d Letter\n ", i, j)

for i in myd:
    print("6.4 For loop, dictonary \n Key : %d \n" % (i))

    for j,i in myd.items():
        print(" Key : %d \n Value :%s\n" % (j,i))

for i in myt:
    print("6.4 For loop, tuple \n ", i)

print("6.4 For loop, tuples \n ")
for i in msg:
    print("%s" % (i))

for i in range(0,5,2):
    print(i)

counter = 5

while counter> 0 :
    print("countdown =:", counter)
    counter = counter-1

j = 0
for i in range(5):
    j += 2
    print('i = %d, j = %d \n' % (i,j))
    if j == 6:
        break
    if j == 6:
 
        k = 0
        for i in range(5):
            k += 2
            print('i = %d, k = %d' % (i,k))
            if k >= 3:
                continue
            print( " if k >=3 this message will be skipped \n")
try:
    answer = 12/0
    print(answer)
except:
    print(" value error can not be devided with zero")

try:
     userInput1 = int(input("Please enter a number: ")) 
     userInput2 = int(input("Please enter another number: ")) 
     answer =userInput1/userInput2 
     print ("The answer is ", answer) 
     myFile = open("missing.txt", 'r')

except ValueError: 
    print ("Error: You did not enter a number") 
except ZeroDivisionError: 
    print ("Error: Cannot divide by zero") 
except Exception as e: 
    print ("Unknown error: ", e)


