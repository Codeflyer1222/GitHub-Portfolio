#include<iostream>  
using namespace std;  
int main()  
{  
string str= "java is the best programming language";  
cout <<  str<<'\n';  
cout <<"Position of the programming word is :";  
if(str.find("programming")){
    cout << "true";
}
return 0;   
}