#include <iostream>
#include <ctime>
#include <cstdlib>
#include <vector>
using namespace std;
vector <int> win;
vector <int> lose;
string computer;
int correct(void){
    win.push_back(1);
    cout << win.size() << "/";
    cout << lose.size();
    return(0);
}
int defeat(void){
    lose.push_back(1);
    cout << win.size() << "/";
    cout << lose.size();
    return(0);
}
int both(void)
{
    cout << win.size() << "/";
    cout << lose.size();
    return(0);
}
int main(void)
{
    vector<int> win;
    vector<int> lose;
    //while loop argument
    bool looping = true;
    //asks the user if they want to continue the program
    string play;
    while(looping)
    {
        cout << "\nDo you want to play a game?\nyes or no:  ";
        cin >> play;
        if(play == "yes")
        {
            //start of game/question
            string ask;
            cout << "\nRock, Paper, or Scissors?\n";
            cin >> ask;
            cout << "You chose " << ask << "\nThe computer chose ";
            //fail-safe error for game
            if(ask == "Rock" || "Paper" || "Scissors")
            {
                  int randNum = 0;
                //seed generator with current time
                srand( time(NULL) );
                randNum = rand() %3 + 1;
                //Computer's choice
                if(randNum == 1)
                {
                    computer = "Rock";
                    cout << computer << "\n";
                }
                else if(randNum == 2)
                {
                    computer = "Paper";
                    cout << computer << "\n";
                }
                else
                {
                    computer = "Scissors";
                    cout << computer << "\n";
                }
                //end of game

                //user wins
                if(ask == "Rock" && computer == "Scissors")
                {
                    cout << "You win\n\nThe total score is: ";
                    correct();
                }
                else if(ask == "Paper" && computer == "Rock")
                {
                    cout << "You win\n\nThe total score is: ";
                    correct();
                }
                else if(ask == "Scissors" && computer == "Paper")
                {
                    cout << "You win\n\nThe total score is: ";
                    correct();
                }
                //computer wins
                else if(computer == "Rock" && ask == "Scissors")
                {
                    cout << "You lost\n\nThe total score is: ";
                    defeat();
                }
                else if(computer == "Paper" && ask == "Rock")
                {
                    cout << "You lost\n\nThe total score is: ";
                    defeat();
                }
                else if(computer == "Scissors" && ask == "Paper")
                {
                    cout << "You lost\n\nThe total score is: ";
                    defeat();
                }
                else if(ask == computer)
                {
                    cout << "You tied with the computer";
                    cout << "\n\nThe total score is: ";
                    both();
                }
                else
                {
                    cout << "something went wrong. The program needs to be fixed";
                }
                
            }
            else
            {
                cout << "Input is invalid\nYou must enter either 'Rock', 'Paper', or 'Scissors'\n\n";
            }
            
        }
        //kills program
        else if ( play == "no")
        {
            cout << "No game today... Goodbye!";
            looping = false;
        }
        //fail-safe error for program
        else
        {
            cout << "Input is invalid\nYou must enter either 'yes' or 'no'\n\n";
        }
        
    }
}