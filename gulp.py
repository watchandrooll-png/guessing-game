
import random
import sys
def game():
    while True:
        try:
            guess = int(input("Guess a number 1-100 \nchoice: "))
        except ValueError:
            print("enter an int you fuckingggg retard")
            continue
    
        if guess > answer:
            print("too high g try again...")
            
        elif guess < answer:
            print("too low g")
        else:
            print(f"congrats g you won.. with ${attempts} attempts")
            break

while True:
    attempts = 0
    choice = input("  ===========\n Choose wisely..\n\n(a) Play\n(b) Quit..\n\nChoice: ")
    if str.lower(choice) == "a":
          answer = random.randint(1,100)
          game()
    elif str.lower(choice) == "b":
        sys.exit()