#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main(void)
{
    ifstream infile;
    string data = "";
    string line = "";

    //Attempt to open file "usernames.txt"
    infile.open("usernames.txt");
    //Verify the file opened successfully
    if( infile.is_open()) {
        cout << "Success N00B!\n";
    }
    //Loop while ther is data in the file
    while(!infile.eof()) {
        //Read the file a line at a time
        getline(infile, line);
        //Append the letter to the end of the string
        data += line + "\n";
    }
    //Display the string with the file contents
    cout << data << endl;
    
    return(0);
}