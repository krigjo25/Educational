name = input("Name : ") # geting the name of the participan
print (" Greetings, ", name, "We will calculate which year you'll turn 100 just follow the next instructions")
age = int(input(" Type your birthday : ")) # retriving the age and converting string into integer
year = (2020 - age + 100) # converts integer to string
print( "Greetings, %s you're %s, in %s you'll be 100 years old" % ( name,  age,  year))
