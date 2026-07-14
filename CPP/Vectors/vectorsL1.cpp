#include <iostream>
#include <vector>
using namespace std;
int main(void){
    vector<int> grades;
    int grade = 0;
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
            grades.push_back( grade );
        }
    }
    int total = 0;
    for( int i = 0; i < grades.size(); i += 1 ){
        cout << "Grade #" << i+1 << " is " << grades.at(i) << "\n";
        total += grades.at(i);
    }
    cout << "The total is: " << total << endl;
    return( 0 );
}