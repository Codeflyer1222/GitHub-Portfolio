#include <iostream>
#include <fstream>

int main(void) 
{
    std::ifstream file ("usernames.txt");

    std::string data;
    std::string line;
    std::string input;
    while(!file.eof()) {
        //Read the file a line at a time
        getline(file, line);
        data += line + "\n";
    }
    std::cout << data;
}