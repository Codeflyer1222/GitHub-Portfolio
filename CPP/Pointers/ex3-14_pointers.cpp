#include<iostream>
using namespace std;
int main(void)
{
    int kakarot = 10;
    int *vegeta = &kakarot;

    *vegeta += 9000;
    
    cout << "Kakarot is: " << kakarot << endl;
}