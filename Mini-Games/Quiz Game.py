#------------------------------------
def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1
    print("---------------------------------------------------------")
    print("QUIZ GAMEZZ !")

    for key in questions:
        print("------------------------------------------------------------")
        print(key)
        for i in options[question_num - 1]:
            print(i)
        guess = input("Enter (A, B, C or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key),guess)
        question_num += 1
    display_score(correct_guesses, guesses)
#------------------------------------
def check_answer(answer, guess):
    if answer == guess:
        print("CORRECT! ")
        return 1
    else:
        print("WRONG!")
        return 0

#------------------------------------
def display_score(correct_guesses, guesses):
    print("------------------------------------------------")
    print("RESULTS")
    print("------------------------------------------------")
    print("Answers: ",end=" ")
    for i in questions:
        print(questions.get(i),end=" ")
    print()

    print("Guesses: ", end=" ")
    for i in guesses:
        print(i, end=" ")
    print()

    score = round(correct_guesses/len(questions)*100)
    print("Your score is: "+str(score)+"%")

#------------------------------------
def play_again():
    response = input("Do you want to play again?(Yes/No):")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False




#------------------------------------

questions = {"What country has the most islands in the world? ": "D",
             "What’s the smallest country in the world? ": "A",
             "What’s the capital of Canada?": "B",
             "Name the largest (not highest) mountain range in the world? ": "B",
             "Where is the lowest natural place on planet Earth? ": "C",
             "Name the longest river in the world? ": "A"}

options = [["A. Egypt", "B. England", "C. Brazil", "D. Sweden"],
           ["A. The Vatican", "B. Rwanda", "C. Mexico", "D. Kenya"],
           ["A. Paris", " B. Ottawa", "C. London", "D. Canberry"], ["A. Mountain of Solomon", "B. The Andes ", "C. Table Mountain", "D. Mount Sinah"],
           ["A. Mountain Teru", "B. Run-way Mountain", "C. The Mariana Trench", "D. Table Mountain"],
           ["A. The Nile", "B. The Amazon", "C. The Oak-ale river ", "D. The Norway river"]]
new_game()

while play_again():
    new_game()
print("Byee!")



