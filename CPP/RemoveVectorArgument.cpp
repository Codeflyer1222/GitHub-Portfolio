//This is the number removal program, created by Sam Brown on 26 Jan 2022.
#include <iostream>
#include <vector>
#include <algorithm>
#include <iterator>
using namespace std;
int main(void){
    vector<int> grades;
    int grade = 0;
    int del = 0;
    cout << "input number 3 numbers: \n";
    cin >> grade;
    grades.push_back(grade);
    cin >> grade;
    grades.push_back(grade);
    cin >> grade;
    grades.push_back(grade);
    copy(grades.begin(), grades.end(), ostream_iterator<int>(cout, " "));
    cout << "\nwhat number do you want to remove? ";
    cin >> del;
    auto iterbegin = std::remove_if(grades.begin(), grades.end(), [del](int val){
        if (val == del){
            return true;
        }
        return false;
    });
    grades.erase(iterbegin, grades.end());

    copy(grades.begin(), grades.end(), ostream_iterator<int>(cout, " "));
    cout << "are your remaining numbers.";
}