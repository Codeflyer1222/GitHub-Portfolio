#include <iostream>
#include <fstream>

int main(void)
{
    std::ofstream file ("hello.txt");

    file << "wazthup!";

    return(0);
}