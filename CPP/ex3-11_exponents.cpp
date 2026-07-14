//This is the exponent calculator program, created by Sam Brown on 1 Febuary 2022.
#include <iostream>
using namespace std;
int compute(int base, int exponent){
    int result = 1;
    while (exponent != 0){
        result *= base;
        exponent -= 1;
    }
    return(result);
}
bool looping = true;
string Continue;
int main(void) {
    while (looping == true){
        cout << "do you want to continue the exponent calculator program?\nEnter Y for yes and N for no: \n";
        cin >> Continue;
        if (Continue == "Y"){
            int base = 0;
            int exponent = 0;
            int result = 0;
            cout << "Enter Base: ";
            cin >> base;
            cout << "Enter Exponent: ";
            cin >> exponent;
            result = compute(base, exponent);
            cout << "Base    : " << base << endl;
            cout << "Exponent: " << exponent << endl;
            cout << "Result   : " << result << endl;
        }
        else if(Continue == "N"){
            cout << "The program is over now";
            looping = false;
        }
        else{
            cout << "Input is invalid. Either type 'Y' or 'N'\n\n";
        }
    }
}