#include <iostream>
using namespace std;
int main(void) {
    string message = "hello all!";
    for (int index = 0; index < message.length(); index ++) {
        cout << message[index];
    }
    cout << endl;
    return 0;
}