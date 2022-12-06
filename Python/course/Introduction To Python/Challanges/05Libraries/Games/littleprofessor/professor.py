import random as r


def main():
  #   Prompting a level input
    lvl = get_level()

    # Calculating the integers

    x = generate_integer(lvl)
    y = generate_integer(lvl)

    n = x + y

    #   Game Configurations
    i = 3
    score = 0

    while True:

        try :
            #   Prompting the user for the output
            prmpt = int(input(f'{x} + {y} ='))

        except ValueError:

            #   Decrease the score by one

            i -= 1
            print('EEE')

            if i == 0: return print(f'Correct number : {n} \n Score : {score}')

        else:

            if prmpt == n:

                #   Adding one point to score
                score += 1

                #   Creating a new math problem to be solved
                x = r.randint(0,10)
                y = r.randrange(0,10)
                n = x + y

            elif prmpt != n:

                print('EEE')
                i -= 1

            #   Breaking out of the loop
            if i <= 0: return print(f'Correct number : {n} \n Score : {score}/9')
            elif score == 9: return print(f'Score : {score}')

def get_level():

    '''
        Choosing the difficulty level,
        the level has to be a positive integer

    '''
    while True:

        try :

            lvl = int(input('level : '))

            if lvl >= 1 and lvl <= 3: return lvl

        except (ValueError, TypeError) as e:print(e)

        else:
            print('Choose a level between 1 & 3')
            continue


def generate_integer(lvl):

    if lvl == 1: return r.randint(0,10)
    elif lvl == 2: return r.randint(10, 99)
    elif lvl == 3: return r.randint(100, 999)


if __name__ == "__main__":
    main()