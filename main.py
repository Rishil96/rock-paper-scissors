from random import randint
from art import rock, paper, scissor


def continue_playing():
    choice = input("Do you want to continue playing? Y or N: ")
    return True if choice.lower() == 'y' else False


hand = {0: rock, 1: paper, 2: scissor}
game_on = True

while game_on:

    user_choice = input("Choose one of the following:- \n0: Rock, 1: Paper, 2: Scissors: ")
    # Check if user choice is valid
    if user_choice not in ["0", "1", "2"]:
        print("Invalid Choice!")
        if continue_playing():
            continue
        else:
            print("Thanks for playing!")
            game_on = False

    user_choice = int(user_choice)
    computer_choice = randint(0, 2)

    print("You played: ")
    print(hand[user_choice])

    print("\nComputer played: ")
    print(hand[computer_choice])

    # Player Wins
    if (user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0) or (user_choice == 2 and computer_choice == 1):
        print("Congrats! You won this round.")
    # Computer Wins
    elif (user_choice == 0 and computer_choice == 1) or (user_choice == 1 and computer_choice == 2) or (user_choice == 2 and computer_choice == 0):
        print("Bad Luck! Computer Wins.")
    # Draw
    else:
        print("Tough Fight! Its a draw.")

    if continue_playing():
        continue
    else:
        game_on = False
        print("Thanks for playing!")
