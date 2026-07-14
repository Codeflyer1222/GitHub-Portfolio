#include <iostream>
#include <vector>
#include <algorithm>
#include <iterator>
using namespace std;
int main(void){
    vector<int> grades;
    int grade = 0;
    int del;
    cout << "input number \n";
    cin >> grade;
    grades.push_back(grade);
    cin >> grade;
    grades.push_back(grade);
    cin >> grade;
    grades.push_back(grade);
    copy(grades.begin(), grades.end(), ostream_iterator<int>(cout, " "));
    cout << "delete a number\n";
    cin >> del;
    del = del -1;
    if(grades == del){
        cout << "true";
        grades.erase(grades.begin() +del);
    }
    copy(grades.begin(), grades.end(), ostream_iterator<int>(cout, " "));

}