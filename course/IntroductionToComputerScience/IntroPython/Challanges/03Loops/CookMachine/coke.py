#   Coke.py

#   Initializing variables
x = 50
c = 0

#   Creating a while loop to iterate the program
while x > 0:

    #   Prompting the use to input a cent
    print(f'amount due : {x}')

    prmpt = int(input('Cent :'))


    if prmpt == 5 or prmpt == 10 or prmpt == 25 or prmpt == 50:
        x -= prmpt

    else:

        #   Warn the user
        print(x)
    if x < 0:
        c -= x


print(f'amount Change : {c}')