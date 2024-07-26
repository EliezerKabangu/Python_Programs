import random

choice = ['A', 'B', 'C']
computer = random.choice(choice)

def new_game():

    guesses = []


    print("---------------------------------------------------------------")
    print("THE CUP G@ME ... |_| |_| |_| |_|...")
    print("---------------------------------------------------------------")
    print("Players are required to guess the location of the marble after the")
    print("marble has been carefully hidden in one of four cups. ")
    print("The player will be given 5 tries for 5 guesses.")

    res = input("Are you ready to play? (Yes/No): ").upper()

    while True:
        if len(res) == 0:
            res = input("Are you ready to play? (Yes/No): ").upper()
        elif res == "YES":
            break
        elif res == "NO":
            print("bYe :) ")
            quit()
        else:
            res = input("Are you ready to play? (Yes/No): ").upper()


    print("---------------------------------------------------------------")
    print("The marble has been secretly hidden in one of these cups.")
    print("Guess 1. . .")
    print("  A      B      C  ")
    print("|   |  |   |  |   |")
    print("|___|  |___|  |___|")
    response = input("Which cup is it?: ").upper()

    guess1 = check_answer(response, computer)
    guesses.append(guess1)

    computer2 = random.choice(choice)

    print("---------------------------------------------------------------")
    print("Guess 2. . .")
    print("The marble has been secretly hidden in one of these cups.")
    print("  A      B      C  ")
    print("|   |  |   |  |   |")
    print("|___|  |___|  |___|")
    response = input("Which cup is it?: ").upper()

    guess2 = check_answer(response, computer2)
    guesses.append(guess2)

    computer3 = random.choice(choice)

    print("---------------------------------------------------------------")
    print("Guess 3. . .")
    print("The marble has been secretly hidden in one of these cups.")
    print("  A      B      C  ")
    print("|   |  |   |  |   |")
    print("|___|  |___|  |___|")
    response = input("Which cup is it?: ").upper()

    guess3 = check_answer(response, computer3)
    guesses.append(guess3)

    computer4 = random.choice(choice)

    print("---------------------------------------------------------------")
    print("Guess 4. . .")
    print("The marble has been secretly hidden in one of these cups.")
    print("  A      B      C  ")
    print("|   |  |   |  |   |")
    print("|___|  |___|  |___|")
    response = input("Which cup is it?: ").upper()

    guess4 = check_answer(response, computer4)
    guesses.append(guess4)

    computer5 = random.choice(choice)

    print("---------------------------------------------------------------")
    print("Guess 5. . .")
    print("The marble has been secretly hidden in one of these cups.")
    print("  A      B      C  ")
    print("|   |  |   |  |   |")
    print("|___|  |___|  |___|")
    response = input("Which cup is it?: ").upper()

    guess5 = check_answer(response, computer5)
    guesses.append(guess5)

    display_score(guesses)

def check_answer(guess, answer):
    if answer == guess:
        print()
        print("  "+answer+"  ")
        print("|   |")
        print("|___|")
        print("Correct! ")
        return 1
    else:
        print()
        print("  " + answer + "  ")
        print("|   |")
        print("|___|")
        print("Wrong! It was hidden in cup "+answer)
        return 0


def display_score(guess):
    print("---------------------------------------------------------------")
    print("RESULTS")
    print("---------------------------------------------------------------")
    print("You managed to get {} out of 5".format(sum(guess)), " guesses.")

def play_again():
    tes = input("Do you want to play again? :").upper()
    if tes == "YES":
        return True
    else:
        return False

new_game()
while play_again():
    new_game()

print("Bye Bye :)")