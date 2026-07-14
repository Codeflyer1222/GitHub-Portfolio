#include<iostream>
using namespace std;
bool compute( int base, int exponent, int * result ) {
    if(exponent <= 0){
        return(false);

    }
    *result = 1;
    while(exponent != 0) {
        /*same thing as 1 times base. We use a pointer instead of a variable in
        this line because if it were a variable, we wouldn't be able to access
        base. base is a local variable that can only work within its own scope, which is inside of main.
        result would also only be able to work within its own scope if it wasn't
        a pointer. But because it's a pointer, it can access outside of its scope.*/
        *result *= base;
        exponent -= 1;
    }
    return( true );
}
int main(void) 
{
    int base = 0;
    int exponent = 0;
    int result = 0;
    cout << "Enter Base: ";
    cin >> base;
    cout << "Enter Exponent: ";
    cin >> exponent;
    if(compute(base, exponent, &result) == false) 
    {
        cerr << "\nExponent must be positive\nOnly use integers, no decimals\n";
    }
    else 
    {
        cout << "Base    : " << base << endl;
        cout << "Exponent: " << exponent << endl;
        cout << "Result  : " << result << endl;
    }
    return( 0 );
}