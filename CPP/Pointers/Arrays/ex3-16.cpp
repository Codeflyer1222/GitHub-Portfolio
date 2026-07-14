#include <iostream>
using namespace std;
int main(void){
    int numbers[10] = {10,20,30,40,50,60,70,80,90,100};
    numbers[5] = 42;
    cout << numbers[5];
}