#include <iostream>
#include <vector>
#include <iterator>
#include "Testing.h"
using namespace std;
int main(void)
{
    Student school;
    vector<string> bag;
    /*if(bag.empty()){
        copy(bag.begin(), bag.end(), ostream_iterator<string>(cout << " \n"));
        string clothes;
        cin >> clothes;
        bag.push_back(clothes);
        copy(bag.begin(), bag.end(), ostream_iterator<string>(cout << " "));
        
    }*/
    string first;
    string last;
    cout << "what is the child's first name?:   ";
    cin >> first;
    cout << "\nwhat is the child's last name?:   ";
    cin >> last;
    school.student(first,last);
    school.Show();
}