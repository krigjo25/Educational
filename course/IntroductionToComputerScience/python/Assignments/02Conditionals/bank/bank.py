#   bank.py

def main():

    #   Prompt the user with a question
    prompt = input('Greetings :')
    x = prompt.lower()

    # Checking wheter the employee greets or not
    if  'hello'in x: print('$0')
    elif x.startswith('h'):print('$20')
    else: print('$100')

main()