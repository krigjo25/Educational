#   Initiating object 'BinaryGame'
class BinaryGame(Game):

    #   Initializing the Initializer
    def __init__(self):
        return

    #   Generate questions method
    def GenerateQuestion():

        ''' 
                GenerateQuestions()
            an Instance method to generates binary questions.

        '''

        #   Importing randint function
        from random import randint

        #   Initializing a local variable called 'Score'
        Score   = 0

        #   Looping through using for loop to evaluate the answer
        for i in range(self._NOQ):

            #   Initializing a variable and choosing a random integer from 1-100
            x = randint(1,100)

            #   Prompt the user to type in an integer
            prmpt = input()

        #   Creating a while loop to loop through a true statement
        while True:

            #   Creating a try, except loop
            try:
                # Converting the string into an integer base 2
                prmpt = int(prmpt, base=2)

                #   Updating the user Score
                Score += 1

                #   Breaking out from the while loop
                break

            except:

                #   Print out an error message
                print('')

                #   Prompting the user to answer again
BinaryGame.GenerateQuestion()