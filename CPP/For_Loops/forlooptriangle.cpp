#include <iostream>
using namespace std;
int main(void){
    for(int y = 0; y < 5; y += 1){
        cout << y << " ";
        for(int x = y; x > 0; x -= 1){
            cout << x  << " ";
        }
        cout << "\n";
    }
    return 0;
}