# functions
# To check if the number is odd or even
def checkIfPrime (numberToCheck):
    for x in range(2,numberToCheck): # Using the variable to check if the number canbe devided by two
        if(numberToCheck%x == 0):
            return False
    return True
