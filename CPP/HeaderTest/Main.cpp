#include <iostream>
using namespace std;
/*#include "HStuff.h"
int main(void){
    warts gum;
    std::cout << gum.function(10,1);
}*/
int main(void){
    int array[3] = {1,2};
    cout << array[0] << endl;
    array[2] = 3;
    cout << array[2] << endl;
    //the below creates a pointer holding the adress of the first value of "array"
    //NEEDS TO BE FIXED
    int *ptr = array;
    //the below records how many elements is in "array"
    int bytes = sizeof(array);
    int count = bytes / sizeof(array[0]);
    cout << "The array is " << count << " elemnts long.\n";
}
