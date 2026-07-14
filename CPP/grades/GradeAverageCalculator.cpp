//This is the Calculator program, made by Sam Brown on 27 Jan 2022.
#include <iostream>
#include <vector>
#include <algorithm>
#include <iterator>
using namespace std;
int main(void){
    vector<int> grades;
    int grade = 0;
    string choice;
    int del = 0;
    bool repeat;
    repeat = true;
    while (repeat == true){
        cout << "1) Enter a new grade\n";
        cout << "2) Show all grades\n";
        cout << "3) Display GPA\n";
        cout << "4) remove a grade\n";
        cout << "0) Exit\n";
        cin >> choice;
        cout << "\n";
        //Allows the user to input an integer
        if ( choice == "1"){
            bool looping = true;
            while( looping == true){
                cout << "Enter a grade ( -1 to quit )\n";
                cin >> grade;
                 if( grade == -1){
                    looping = false;
                }
                else if( grade < 0 || grade > 100){
                    cout << "Grade out of range!\n";
                }
                else {
                    grades.push_back(grade);
                }
            }
        }
        //Dislplays user's input
        else if(choice == "2"){
            cout << "your grades are: ";
            copy(grades.begin(), grades.end(), ostream_iterator<int>(cout, " "));
            cout << " out of " << grades.size() << " grades\n\n";
        }
        //Displays user's input after being calculated as a grade
        else if(choice == "3"){
            int average = 0;
            int total = 0;
            for( int i = 0; i < grades.size(); i += 1 ){
             total += grades.at(i);
            }
            cout << "The total is: " << total << "\n" << endl;
            average = total / grades.size();
            cout << "The average is: " << average << "\n" << endl;
            if(average >= 90 && average <= 100){
                cout << "Your average is an A.\n\n";
                
            }
            else if( average >= 80 && average <= 89){
                cout << "Your average is a B.\n\n";
            }
            else if(average >= 70 && average <= 79){
                cout << "Your average is a C\n\n";
            }
            else if(average >= 60 && average <= 69){
                cout << "Your average is a D\n\n";
            }
            else {
                cout << "Your average is a F.\n\n";
            }
        }
        //Delets chosen argument
        else if( choice == "4"){
        cout << "\nwhat number do you want to remove? ";
        copy(grades.begin(), grades.end(), ostream_iterator<int>(cout, ", "));
        cin >> del;
        auto iterbegin = std::remove_if(grades.begin(), grades.end(), [del](int val){
            if (val == del){
                return true;
            }
            return false;
        });
        grades.erase(iterbegin, grades.end());

        }
        //Ends program
        else if (choice == "0") {
            cout << "Good-bye!\n\n";
            repeat = false;
        }
        //If user doesn't input one of the menu options
        else{
            cout << choice << " is not a valid menu option.\n\n";
        }
    }
}