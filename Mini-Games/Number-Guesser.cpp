#include<iostream>
#include<ctime>

int main(){

    int player;
    int computer;
    int tries;

    srand(time(NULL));
    computer = rand() % 100 + 1;

    std::cout << "|------------NUMBER GUESSING GAME---------------|\n";
    std::cout << "A number has been picked at random.\n";
    std::cout << "Try and figure out which number it is !!\n" << '\n';
    do{
    std::cout << "<----|o|-------|o|-------|o|----->\n";
    std::cout << "Enter a guess: ";
    std::cin >> player; 
    tries++;

    if (player > computer){
        std::cout << "Your guess is too high !\n";
    }
    else if (player < computer){
        std::cout << "Your guess is too low !\n";
    }
    else{
        std::cout << "You've guessed it! The number is " << computer <<".\n" << '\n';
        
    }
    }while(player != computer);

    std::cout << "Number of guesses: " << tries;

    return 0;
}



