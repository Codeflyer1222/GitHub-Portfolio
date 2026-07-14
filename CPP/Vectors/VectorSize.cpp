#include <vector>
#include <iostream>
using namespace std;
vector <int> win;
vector<int> lose;
int function(void)
{
    vector <int> ham;
    ham.push_back(3);
    ham.push_back(4);
    cout << ham.size();
    return(0);
}
int correct(void){
    win.push_back(1);
    cout << win.size() << "/";
    cout << lose.size();
    return(0);
}
int defeat(void){
    lose.push_back(1);
    cout << win.size() << "/";
    cout << lose.size();
    return(0);
}
int main(void)
{
    correct();
}