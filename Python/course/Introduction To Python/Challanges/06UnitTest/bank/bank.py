def main():

    #   Prompt the user with a question
    try :
        prompt = str(input('Greetings :'))
    except ValueError as e:
        print(e)

    prompt.lower()
    print(value(prompt))

    return

def value(arg):

    #   Initalizing a list
    if 'hello'in arg: return 0
    elif arg.startswith('h'):return 20
    else: return 100

if __name__ == '__main__':
    main()