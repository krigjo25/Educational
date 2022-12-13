#   playback.py

#   defining a function that prompts the user for inputs

def PromptPlayBack():

    # Initialize variables & prompt the user
    a = input('')

    #   Replace the whitespaces with 3 periods
    a = a.replace(' ', '...')

    print(a)

    return

PromptPlayBack()
