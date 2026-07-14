#include <iostream>
#include <fstream>
using namespace std;

int main(void) 
{
    ofstream outfile;
    string data = "";
    string line = "";
    bool looping = true;

    while( looping == true ) {
        cout << "Type a name (Q/q to quit): ";
        getline(cin, line);
        if( line == "q" || line == "Q" ) {
            looping = false;
        }
        else {
            data += line + "\n";
        }
    }
    //Attempt to open the usernames.txt file for writing.
    outfile.open("usernames.txt", ios::app);
    //Validate the opened successfully
    if (outfile.is_open()) {
        cout << "success N00B!";
    }
    //Save all enterd names to the file then close it
    outfile << data;
    return (0);
}