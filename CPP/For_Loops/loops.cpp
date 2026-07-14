#include<iostream>
using namespace std;
int main(void)
{
    string choice;
    bool looping = true;
    while (looping == true) {
        cout << "1) menu option A\n";
        cout << "2) Menu option B\n";
        cout << "0) Quit\n";
        cin >> choice;
        if (choice == "1") {
            cout << "Option A selected.\n";
        }
        else if (choice == "2") {
            cout << "Option B selected.\n";
        }
        else if (choice == "0") {
            cout << "Good-bye!\n";
        }
        else {
            cout << "Uknown option(" << choice << ")\n";
        }
    }
    return 0;
}