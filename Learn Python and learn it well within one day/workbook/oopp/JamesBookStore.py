'''
Question 4 :

Class NameManglingDemo:
    def __init__(self):
        self.__myData = 1
In the code above, myData is preceded by two leading underscores. What is the Mangled
name for myData?

 // PmyData?
'''
'''
Question 5 :

* What is the difference between a class variable and an instance variable?

** With reference to the code below, list the instance and class variable(s).

class Book
    message = 'Welcome to E-books online'

    def __init__(self, pTitle, pAuthor, pPrice):
        self.title = pTitle
        self.author = pAuthor
        self.price = pPrice

    def __str__(self):
        return 'Title: %s \nAuthor: %s \n Price: %.2f' % (self.tile, self.author, self.price)

**** With the reference to the Book class in b, determind the output of the code below,
    with-out running the code:
aRomancebook = Book('Sunset','Jhon Doe', 10)
aSciFiBook = Book('Vizvaz', 'Bruce Lee', 10)

aRomanceBook.price = 20
print(aRomanceBook.price)
print(aSciFiBook.price)

Book.message = 'Online Books'
print(aRomanceBook.message)
print(aSciFiBook.message)
'''
class JamesBookStore:
    message = 'Welcome to E-books online'

    def __init__(self, pTitle, pAuthor, pPrice):
        self.title = pTitle
        self.author = pAuthor
        self.price = pPrice
        print("%s added to the bookshelf " % (self.title))

    def __str__(self):
        return 'Title: %s \nAuthor: %s \n Price: %.2f $' % (self.title, self.author, self.price)
# Question 5.2
 # // Object = Class(self.title, self.author, self.price)
aRomanceBook = JamesBookStore('Sunset', 'Jhon Doe', 10)
aSciFiBook = JamesBookStore('Vizvaz', 'Bruce Lee', 10)

 # Question 5.3
 # Callout to price
 #//Object.price = 20 dollars
aRomanceBook.price = 20
print(aRomanceBook.price)
print(aSciFiBook.price)

# Class.Variable
JamesBookStore.message = 'Online Books'
print(aRomanceBook.message)
print(aSciFiBook.message)

print(aRomanceBook, "\n")
print(aSciFiBook)
