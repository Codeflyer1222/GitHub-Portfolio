#include <iostream>
#include <vector>
#include <iterator>
#include "gradesClass.h"
using namespace std;
float gpa;
int main(void){
    vector<int> grades;
    int grade = 0;
    int del = 0;

    bool repeating = true;
    while(repeating == true)
    {
        cout << "enter 1,2,3,4, or 5\n\n";
        cout << "1) Modify student profile\n";
        cout << "2) Add new grade for student profile\n";
        cout << "3) calculate GPA for student profile\n";
        cout << "4) Show all grades for student profile\n";
        cout << "0) End Program\n";
        int choice;
        cin >> choice;
        Student school;
        //this is where the student profile is created
        if (choice == 1)
        {
            //this is where you put in the class object and methods. Use the "Show()" method.
            //This program only holds one student profile at a time and only holds the data for
            //as long as the program is running.

            string first;
            string last;
            cout << "what is the child's first name?:   ";
            cin >> first;
            cout << "\nwhat is the child's last name?:   ";
            cin >> last;
            school.student(first,last, gpa);
            school.Show();

            
        }
        //this is where the user adds a grade to the grades vector
        else if(choice == 2)
        {
            bool looping = true;
            while( looping == true){
                cout << "Enter a grade ( -1 to quit )\n";
                cin >> grade;
                 if( grade == -1){
                    looping = false;
                    school.save(grades);
                }
                else if( grade < 0 || grade > 100){
                    cout << "Grade out of range!\n";
                }
                else {
                    grades.push_back(grade);
                }
            }
        }
        
        //this is where the gpa is dividendculated and added to the student profile
        else if(choice == 3)
        {
            //copy and paste the code from the GradeAverageClaculator program here
            int average = 0;
            int total = 0;
            //go into each individual value in the grades vector and
            //run one iteration of the code per many values inside of
            //the vector. With every iteration, it will spit out a letter
            //grade, in turn, creating multiple letter grades.
            float dividend = 0.0;
            float divisor = 0.0;
            for( int i = 0; i < grades.size(); i += 1 ){
                total += grades.at(i);
                if(grades.at(i) >= 90 && grades.at(i) <= 100){
                    cout << "grade " << i + 1 << " has the letter grade A \n";
                    dividend += 4.0;
                    divisor += 1;
                }
                else if( grades.at(i) >= 80 && grades.at(i) <= 89){
                    cout << "grade " << i + 1 << " has the letter grade B \n";
                    dividend += 3.0;
                    divisor += 1;
                }
                else if(grades.at(i) >= 70 && grades.at(i) <= 79){
                    cout << "grade " << i + 1 << " has the letter grade C \n";
                    dividend += 2.0;
                    divisor += 1;
                }
                else if(grades.at(i) >= 60 && grades.at(i) <= 69){
                    cout << "grade " << i + 1 << " has the letter grade D \n";
                    dividend += 1.00;
                    divisor += 1;
                }
                else {
                    cout << "grade " << i + 1 << " has the letter grade F \n";
                }
            }
            //the average is calculated and displayed here
            average = total / grades.size();
            cout << "\nThe average is: " << average << "\n" << endl;

            //the gpa is calculated and displayed here
            gpa = dividend/divisor;
            cout << "the gpa is: " << gpa << endl << endl;
        }
        //this will show each individual grade
        else if (choice == 4)
        {
            //code is copied and pasted from the other program
            /*cout << "your grades are: ";
            copy(grades.begin(), grades.end(), ostream_iterator<int>(cout, " "));
            cout << " out of " << grades.size() << " grades\n\n";*/
            school.load();
        }
        //ends program
        else if (choice == 0)
        {
            cout << "program finished\n\n";
            repeating = false;
        }
        //error if something went wrong
        else
        {
           cerr << "incorrect input. Type one of the valid numbers"; 
        }
        

    }
}