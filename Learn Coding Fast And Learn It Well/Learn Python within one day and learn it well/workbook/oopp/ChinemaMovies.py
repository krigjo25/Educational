'''
Question 8:

Create a class called Movies that stores 
information about movies. The class should store
the following information: the title of the movie
genre, the main language it is in, the director(s)
and the year it was first released.

The class should also have the __init__ and __str__
methods.

In addition, the class should have a property that
allow users to get and set the genre of the movie.
The setter method should only allow users to set the
genre to 'Romance', 'Action', 'Drama', 'Thriller' or
'Horror'. If the user tries to set the genre to
anything else, the setter method should display
an appropriate error message to the user.

Next, we need an instance method called 
recommendMovie() that recommends users a new movie
based on the genre of th instance used to call the 
method.

If the genre is 'Romance', the movie 'First Date'
is recommended.

If the genre is 'Action', the 'Mutant' is 
recommended.

If the genre is 'Drama', the movie 'The Awakening'
is recommended.

If the genre is 'thriller', the movie 'Mr.K'is 
recommended.

If the genre is 'Horror', the movie 
'A walk down Dawson Street' is recommended.

This method should display the recommended 
movie on the screen.

Save the code above into a file called movie.py

After creating mov1, set its genre to 'Fantasy'.
This should fail.
Next, set the genre to 'Romance' and print a string
representation of mov1.

Finally use mov1 to call the recommendMovie() method.


'''
class ChinemaMovies:
    def __init__(self, pTitle, pGenre, pLang, pRelese, pDir, pYear):
        self.title = pTitle
        self.genre = pGenre
        self.lang = pLang
        self.release = pRelese
        self.dir = pDir
        self.yy = pYear
        print("Movie created")

    def __str__(self):
        return 'Title: %s \nGenre: %s \nOriginal language: %s\nDirected by: %s\n Released: %s %s' % (self.title, self.genre, self.lang, self.dir, self.release, self.yy)

    def SetMovie(self):
        # // User selectes the input 
        prompt = input("Select your genre :") # Setter method
            # // Modifying the string, removing the first part of the input
        i = prompt.replace("Select your genre :", "")
        if i == 'Action' or i == 'Horror' or i == 'Romance' or i == 'Thriller':
                self.genre = i
                return self.genre
        else:
                print("Your selected title doesn't exist ! ")
                prompt = input("select a new title: ")
                i = prompt.replace("Select a new title:", "")
                self.genre = i
                return self.genre
        
# Gettermethod gets the setted movie
    def RecommendMovie(self): # Getter method
        x = self.genre 
        movie = 'Recommended movie : '

        if x == 'Action':
           print("You Selected:", x, movie, "Teen Mutant")
        elif x == 'Drama':
            print("Gilmore Girls")
        elif x == 'Horror' :
            print(movie, "A Nightmare hunter")
        elif x == 'Romance':
                print(movie, " A Day Without You")
        elif x == 'Thriller':
            print(movie, " Mr.K ")
        else:
            print("We're regret to inform the selected genre doesnt exist, feel free to choose a new one")
            

chinema = ChinemaMovies( 'Awakning', '0', 'Norwegian', 241014, 'Jhon Wick', 2014)
print(chinema)
chinema.SetMovie()
chinema.RecommendMovie()
