//This is the Thermometer program, created by Sam Brown on 22 Nov 2021.
#include<iostream>
using namespace std;
int main(void)
{   string tem;
    float K;
    float C;
    float F;
    string choice;
    bool looping = true;
    while (looping == true){
        cout << "1) from Celcius to Farenheit\n";
        cout << "2) from Farenheit to Celcius\n";
        cout << "3) from Celcius or Farenheit to Kelvin\n";
        cout << "0) Quit\n";
        cin >> choice;
        if (choice == "1") {
            cout << "From Celcius to Farenheit selected.\nwhat temperature is it?\n\n";
            cin >> C;
            float F = C * 9/5 + 32;
            cout << "The temperature is " << F << " farenheit degrees\n\n";
        }
        else if (choice == "2") {
            cout << "From Farenheit to Celcius selected.\nwhat temperature is it?\n\n";
            cin >> F;
            float C = (F - 32) * 5/9;
            cout << "The temperature is " << C << " celcius degrees\n\n";
        }
        else if (choice == "0") {
            cout << "Good-bye!\n\n";
            looping = false;
        }
        else if (choice == "3") {
            cout << "From Celcius or Farenheit to Kelvin selected.\nare you in farenheit or celcius temperatures?\n";
            cin >> tem;
            if (tem == "celcius" || tem == "Celcius") {
                cout << "what temperature is it?\n\n";
                cin >> C;
                K = C + 273.15;
                cout << "The temperature is " << K << " kelvin degrees\n\n";
            }
            else if (tem == "farenheit" || tem == "Farenheit") {
                cout << "what temperature is it?\n\n";
                cin >> F;
                C = (F - 32) * 5/9;
                K = C + 273.15;
                cout << "The temperature is " << K << " kelvin degrees\n\n";
            }
            else {
                cout << "Uknown option(" << tem << ")\n\n";
            }
        }
        else {
            cout << "Uknown option(" << choice << ")\n\n";
        }
    }
}