#include <iostream>
using namespace std;
int main (void) 
{
    //
    int current = 0;
    int maximum = 1;
    //I do not understand how "new" works.
    int *grades = new int[maximum];
    bool adding = true;
    //To end program
    cout << "Type -1 to finish entering grades.\n";
    while(adding == true) {
        if(current >= maximum){
            //maximum is doubled which means the array is also doubled?
            maximum *= 2;
            //*temp is given that value of grades. Not it's address.
            int *temp = grades;
            //grades is given a new, larger array.
            grades = new int[maximum];
            //Fail-Safe
            if(grades==NULL) {
                //same thing as cout
                cerr << "Array of " << maximum*4 << " bytes failed.\n";
                exit(1);
            }
            //increases how large the array is by however much "current" has increased
            for(int i = 0; i < current; i+= 1){
                grades[i] = temp[i];
            }
            //frees the data in "temp"
            delete [] temp;
        }
        //displays to the screen
        //1 is added to current for this line but this does not permanently change current
        cout << "Enter Grade #" << current+1 << " :";
        int grade = 0;
        cin >> grade;
        //To end program
        if(grade == -1){
            adding = false;
        }
        //creates the array grades
        else {
            grades[current] = grade;
            //current's value is increased by 1 permenantly because there is both a + and a = sign.
            current += 1;
        }
    }
    //varaible holding the average of all of the grades
    int average = 0;
    //Displays each grade value in the array grades for when the program is finished.
    for(int i = 0; i < current; i += 1) {
        cout << "Grade #" << i+1 << " is: " << grades[i] << endl;
        average += grades[i];
    }
    cout << "the average of the grades is " << average/current << endl;
    delete [] grades;
    return 0;
}