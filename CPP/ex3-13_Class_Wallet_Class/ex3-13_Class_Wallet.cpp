#include <iostream>
#include "Class.h"
using namespace std;
// Include the Wallet class here!

int main(void) {
    Wallet wal;
    bool looping = true;
    string choice;
    int temp = 0;
    while(looping == true) {
        cout << "You have $" << wal.GetTotal() << "\n";
        cout << "1) Modify Quarters\n";
        cout << "4) Modify Pennies\n";
        cout << "0) Quit\n";
        cout << "> ";
        cin >> choice;
        if( choice == "1" ) {
            cout << "Enter new quarter amount\n> ";
            cin >> temp;
            wal.SetQuarters( temp );
        }
        else if( choice == "4" ) {
            cout << "Enter new pennies amount\n> ";
            cin >> temp;
            wal.SetPennies( temp );
        }
        else if(choice == "0" ) {
            looping = false;
        }
        else {
            cout << choice << " - Invalid option..\n";
        }
    }//Closes main program loop
    return 0;
}