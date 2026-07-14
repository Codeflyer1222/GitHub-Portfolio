#include <iostream>
using namespace std;
int main(void){
    int favNum = 0;
    string fullname = "";
    cout << "Enter your favorite number: ";
    cin >> favNum;
    cout << "Enter your first and last name: ";
    ws(cin);
    getline( cin, fullname );
    cout << fullname<< "'s favorite number: " << favNum << "!\n";
    return (0);
}