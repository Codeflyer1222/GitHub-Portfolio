#include <iostream>
#include <vector>
#include <fstream>
using namespace std;
class Student {
private:
    string fname;
    string lname;
    float gpa;
    vector<float> points;
public:
    student() {
        this->fname = "";
        this-> lname = "";
        this->gpa = 0.0;
        return(1);
    }
    student(string f, string l, float g) {
        this->fname = f;
        this->lname = l;
        this->gpa = g;
        return(1);
    }
    void Show(void)
    {
        cout << "First: " << this->fname << endl;
        cout << "Last : " << this->lname << endl;
        cout << "GPA  : " << this->gpa << endl << endl;
    }
    //add the method save. it will contain
    //outfile properties to write data about the student's
    //profile
    save(vector<int> grades) {
        //outfile
        ofstream outfile;
        cout << "Enter your first name: ";
        string tempFname;
        cin >> tempFname;
        cout << "Enter your last name: ";
        string tempLname;
        cin >> tempLname;
        string filename = tempFname + "." + tempLname + ".dat";
        //Attempt to open the usernames.txt file for writing.
        outfile.open(filename, ios:: app);
        //Validate the opened successfully
        if (outfile.is_open()) {
            cout << "file successfully opened\n";
        }
        //Save each individual grade in the file
        for(int grade : grades)
        {
            outfile << grade << endl;
        }
        return true;
    }
    bool load(void) {
        string data = "";
        string line = "";
        cout << "Enter your first name: ";
        string tempFname;
        cin >> tempFname;
        cout << "Enter your last name: ";
        string tempLname;
        cin >> tempLname;
        string filename = tempFname + "." + tempLname + ".dat";
        ifstream infile(filename.c_str());
        if( infile.is_open()) {
            cout << "file successfully opened\n";
        }
        while(!infile.eof()) {
            //Read the file a line at a time
            getline(infile, line);
            //Append the letter to the end of the string
            data += line + "\n";
        }
        cout << data << endl;
        return true;
    }
};