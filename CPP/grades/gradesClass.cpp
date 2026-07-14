#include <iostream>
#include <vector>
using namespace std;
class Student {
private:
    string fname;
    string lname;
    float gpa;
    vector<float> grades;
public:
    Student() {
        this->fname = "";
        this-> lname = "";
        this->gpa = 0.0;
    }
    Student(string f, string l) {
        this->fname = f;
        this->lname = l;
        this->gpa = 0.0;
    }
    void Show(void)
    {
        cout << "First: " << this->fname << endl;
        cout << "Last : " << this->lname << endl;
        cout << "GPA  : " << this->gpa << endl;
    }
};