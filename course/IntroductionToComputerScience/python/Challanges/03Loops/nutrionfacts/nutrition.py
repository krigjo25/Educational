#   Nutrrion.py
def NutritionFacts():

    #   Initializing variables

    #   Creating a dicitionary
    dictionary = {
                    'kiwifruit':90,
                    'lemon': 15,
                    'apple':130,
                    'grapes':90,
                    'orange':80,
                    'peach': 60,
                    'pear': 100,
                    'avocado':50,
                    'banana':110,
                    'honeydew':50,
                    'pinapple':50,
                    'tangerine':50,
                    'nectarine':60,
                    'cantaloupe':50,
                    'grapefruit':60,
                    'watermelon':80,
                    'strawberries':50,
                    'sweet cherries':100
    }

    #   prompting the user
    while True:

        try : x = str(input('Fruit :')).lower()

        except ValueError as e: print(e)

        else:

            #   Exit the code

            if x.isdigit() or x not in dictionary:return

            elif x in dictionary: return print(f'Calories : {dictionary.get(x)}')

#   Calling the function
NutritionFacts()