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

'''
This function counts to 100
'''
 # Defining the function, Request a number from user, remove strings.
def SpellNr(uirn):
    uinr = input("Type a number between 1-999 : ")
    uinr = uinr.replace('Type a number between 1-999:', '')

    # Checking wheter the user inserted 0 or less. And above 1000
    while True: # WHile the condition is true run forever
        try:
            uinum = int(uinr)
            if uinum <= 0:
                print("The number entered is to low")
                uinr = input("Type a number between 1-999: ")
                
            elif uinum > 999:
                print("The number entered is to high")
                uinr = input("Type a number between 1-999: ")
                
        except ValueError:
            uinr = input("You entered an invalid value. Type a number between 1-999 :")
            uinr.replace("Type a number between 1-999: ", '')
        break        # stops the while loop
    print(uinr)
# Getting the length of uinr
    uiLength = len(uinr)
    txt = ''
    
#Creating a dictionary for the unit, tens
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

    # Printing the message
    
    # Get the digits for each value
    units = uinr[uiLength - 1] if uiLength >= 1 else '0' # 1-9 Units
    tens = uinr[uiLength - 2] if uiLength >= 2 else '0' # 10-90  Tens
    hundreds = uinr[uiLength - 3] if uiLength >= 3 else '0' # 100 - 900 Hundreds
   # thousand = uinr[uiLength - 4] if uiLength >= 4 else '0' # 1000 -900 000 Thousand
    '''
    Part 2
    '''
    
    # Printing the digits
    
    if (hundreds != '0'):
        txt = txt + umap[hundreds] + 'Hundred'
    
    # Adding 'and' where its necessary
    if (int(uinr) > 99 and int(uinr) % 100 != 0):
        txt = txt + 'and'
        
    # Printing the tens
    if (tmap == '1'):
        txt = txt + tmap[tens + umap]
    elif (tmap == '0'):
        txt = txt + umap[units]
        # returning the result to a string
    return txt


print(SpellNr(78)).strip()
