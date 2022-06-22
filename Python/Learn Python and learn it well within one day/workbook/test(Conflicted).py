import math

'''
Project 1 :

Part 1 :

Now that you've completed the exercises for all the chapters, let's work on two
projects.

Spelling out numbers part 1
(Number_spelling.py)

The first project is easy to explain:

We need to write a program that spells out any integer up to 3 digits
(i.e any integers less than 1000).
For instance, if the user keys in 729, the program should behave:

Seven hundred and Twenty nine.

Tou can use any of the concepts you've learned in the previous chapters. Try
To coding it yourself. If you're stuck, you can refer to the suggested solution
for help.

Part 2
'''
 # Defining the function, Request a number from user, remove strings.
def SpellNr():
    uinr = input("Type a number between 1-999 : ")
    uinr.replace('Type a number between 1-999 :','')

    # Checking wheter the user inserted 0 or less. And above 1000
    while uinr <= '0' or uinr > '999':
        try:
            if uinr <= '0':
                print("The number entered is to low")
                uinr = input("Type a number between 1-999: ")
                uinr = int(uinr)
                
            elif uinr > '999':
                print("The number entered is to high")
                uinr = input("Type a number between 1-999: ")
                
        except ValueError:
            uinr = input("You entered an invalid value, Type a number between 1-999 :")
            uinr.replace("Type a number between 1-999: ", '')
            
# Getting the length of uinr
    uiLength = len(uinr)
#Creating a dictionary for the units, teens, tens
    umap = {
                0:'Zero',
                1:'One',
                2:'Two',
                3:'Three',
                4:'Four',
                5:'Five',
                6:'Six',
                7:'Seven',
                8:'Eight',
                9:'Nine',
                10:'Ten',
                11:'Eleven',
                12:'Twelve',
                13:'Thirteen',
                14:'Fourteen',
                15:'Fifteen',
                16:'Sixteen',
                17:'Seventeen',
                18:'Eighteen',
                19:'Nineteen'}
    
    tmap = {
                0:'',
                1:'Twenty',
                2:'Thrity',
                3:'Fourty',
                4:'Fifthty',
                5: 'Sixty',
                6:'Seventy',
                7:'Eighty',
                8:'Ninty'}

    
    if uiLength <= 2:
        uinr = int(uinr)
        print(umap[uinr])
             
        

                        
SpellNr()