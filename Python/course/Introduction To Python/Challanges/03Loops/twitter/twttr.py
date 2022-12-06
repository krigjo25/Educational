#   Initializing a list
x = [
        'A', 'E',
        'I', 'O',
        'U', 'a', 'e',
        'i', 'o', 'u',
    ]

#   Promting the user to input a text
prmpt = input('prompt :')


#   Iterating throught the string
for i in prmpt:

    #   Checking if there is a vowel in the string
    if i not in x:

        #   Handling the string
        i = str(i.replace(f'{i}', ''))
        i.strip()

    #   Printing the output
    print(i, end= '')