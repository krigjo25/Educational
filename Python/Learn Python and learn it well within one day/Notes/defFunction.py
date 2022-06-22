'''
Program :
    Defined functions for Learn python and learn it well with-in one day


What is Prime / Odd
 Prime numbers is Integers whom can divide on it self. 
  Odd numbers can neither divide on it self, 
Author
    @krigjo25


'''

# variable declarations

msg = "Hello Word !"


def isPrime(num):
    '''
    About isPrime
    The function checks wheter the value is prime or not
    '''
    for x in range(2, num):
    
        if num % x == 0:
            return 'ODD', False
        
    return 'Prime', True


def varScope(var):
    '''
    About varScope
    Write the difference between global or local message
    '''
    message = var
    print (" He shouts «%s» outside, while the girl said in the class room «%s»" % (msg, message))

def addNum(*args):

        sum = 0
        for i in args:
            sum += i
        print(sum)