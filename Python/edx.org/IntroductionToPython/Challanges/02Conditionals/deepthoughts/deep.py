##  Deep.py         Passed the test 

def main():

    prompt = input('What is the Answer to the Great Question of Life, the Universe, and Everything? :')

    #   Handling the string
    prompt = prompt.replace('-', ' ').lower()

    #   Conditionals
    if '42' in prompt or 'forty two' in prompt:
        print('Yes')

    else: print('No')


main()