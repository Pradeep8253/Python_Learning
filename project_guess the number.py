
from random import randint

EASY_LEVEL_TURNS =10
HARD_LEVEL_TURNS =5
#functions to check user's guess against actual number .
def check_answer(guess , answer , turns):
    """checks answer against guess . returns the number of turns remaining ."""
    if guess>answer:
        print("too high .")
        return turns-1
    elif guess<answer:
        print("too low .")
        return turns-1
    else:
        print(f" you got it ! the answer was {answer}")


#  make function to set difficulty
def set_dificulty():
    level=input("choose a difficulty . type 'easy' or 'hard':")
    if level=="easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    n1 = """
                                      __  __                                  __             
       ____ ___  _____  __________   / /_/ /_  ___     ____  __  ______ ___  / /_  ___  _____
      / __ `/ / / / _ \/ ___/ ___/  / __/ __ \/ _ \   / __ \/ / / / __ `__ \/ __ \/ _ \/ ___/
     / /_/ / /_/ /  __(__  |__  )  / /_/ / / /  __/  / / / / /_/ / / / / / / /_/ /  __/ /    
     \__, /\__,_/\___/____/____/   \__/_/ /_/\___/  /_/ /_/\__,_/_/ /_/ /_/_.___/\___/_/     
    /____/                                                                                   
    """
    print(n1)

    # choose a  random number between 1 to 100

    print(" welcome to the number guessing game !")
    print(" i'm thinking  of a  number between 1 to 100. ")
    answer = randint(1 , 100)
    print(f" the correct answer is {answer}")

    turns = set_dificulty()

    # repeat the guessing functionality if they got it wrong .
    guess=0
    while guess !=answer:
       print(f"you have {turns} attempts remaining to  guess the number .")
       # let the user guess a number
       guess= int(input("make a guess : "))

       turns= check_answer(guess , answer , turns)
       if turns==0:
         print(" you've run out of guesses , you lose .")
         return
       elif guess != answer:
           print("guess again.")
game()



