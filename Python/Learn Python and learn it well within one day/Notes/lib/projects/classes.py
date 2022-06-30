
#   Initiating object 'Game'
class Game():

    #   Initializing the Initializer
    def __init__(self, NOQ = 0):

        self._NOQ = NOQ

        return

    #   Declare a property 
    @property
    def NoQuestions(self):

        return self._NOQ

    @NoQuestions.setter
    def NoQuestions(self, value):

        #   If the value is less than 1
        if value < 1:

            #   add a initial value to the instance variable 
            self._NOQ +=1

            return print('Minimum Number of questions is 1')

        #   If the value is greater than 10
        elif value > 10:

            #   add a initial value to the instance variable 
            self._NOQ = 10

            return print('Maximum number of question is 10')

        else:

            self._NOQ = value

        return self._NOQ

#   Initiating object 'BinaryGame'
class BinaryGame(Game):

    #   Initializing the Initializer
    def __init__(self, NOQ = 0):

        return

#   Initiating object 'MathGame'
class MathGame(Game):

    #   Initializing the Initializer
    def __init__(self, NOQ = 0):

        return

