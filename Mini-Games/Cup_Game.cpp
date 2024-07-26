#include <iostream>
#include<ctime>

char getCharacter(int computer);
void checkAnswer(char player, char computer);
void displayScore(int score, int tries);

int main(){

    char computerChoice;
    char guess;
    int number;
    int score = 0;
    int tries;

    srand(time(NULL));

    std::cout << "<----------------------------------------------->\n";
    std::cout << "********** Welcome to the Cup Game !! ***********\n";
    std::cout << "<----------------------------------------------->\n";
    std::cout << "A marble has been secretly placed in one of three cups. \n";
    std::cout << "Players will be tasked to determine the location of the marble \n";
    std::cout << "You will be given 5 guesses";
    std::cout << '\n';

    for (int i = 0; i < 5 ; i++){
        tries++;

        std::cout << "<-----------|E|----------|E|---------|E|--------->\n";
        std::cout << "Guess " << i + 1 << ". . . \n";
        std::cout << "The marble has been placed in one these cups \n";
        std::cout << "  A        B        C     \n";
        std::cout << "|   |    |   |    |   |   \n";
        std::cout << "|___|    |___|    |___|   \n";
        std::cout << "Which cup is it?: ";
        std::cin >> guess;

        number = rand() % 3 +1;
        computerChoice = getCharacter(number);

        if (guess == computerChoice){
            score++;
        }

        checkAnswer(guess, computerChoice);


    }

    displayScore(score, tries);
    

    return 0;
}

char getCharacter(int computer){
        switch(computer){
        case 1: return 'a';
        case 2: return 'b';
        case 3: return 'c';
        default: std::cout << "Enter a valid choice !!";
    }
}


void checkAnswer(char player, char computer){

    if (player == computer){
        std::cout << "CORRECT !!\n";
        
    }

    else{
        std::cout << "WRONG !!\n";
        std::cout << "It was in cup " << computer << '\n';
    }

}

void displayScore(int score, int tries){

    std::cout << "********RESULTS**********\n";
    std::cout << "Correct guesses: "<< score << '\n';
    std::cout << "Number of guesses: 5" << '\n' << '\n';

    std::cout << "Score: " << double(score)/5 * 100 << " %" ;
}


