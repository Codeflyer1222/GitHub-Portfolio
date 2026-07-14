#include <iostream>
using namespace std;
int main(void)
{
    float userNum = 0.0;
    cout << "Enter a number: ";
    cin >> userNum;
    if ( userNum > 0)
    {
        cout << "That is bigger than zero\n";
    }
    else
    {
        cout << "das not wut I want\n";
    }
}