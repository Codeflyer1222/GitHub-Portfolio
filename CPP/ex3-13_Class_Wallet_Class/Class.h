//this is the header file. It only holds declarations.
#pragma once
class Wallet{
    private:
    //class Variables
    int quarters;
    int pennies;
public:
    //Constructor(s)
    Wallet(void) {
        this->quarters = 0;
        this->pennies = 0;
    }
    Wallet(int quarters) {
        this ->quarters = quarters;
        this->pennies = 0;
    }
    //Destructor
    ~Wallet(void) {
    }
    //Setters
    void SetQuarters(int quarters) {
        this->quarters = quarters;
    }
    void SetPennies(int pennies) {
        this->pennies= pennies;
    }
    //Getters
    int GetQuarters(void) {
        return(this->quarters);
    }
    int GetPennies(void) {
        return(this->pennies);
    }
    //Other functions
    float GetTotal(void) {
        float total = 0.0;
        total += this->quarters * 0.25;
        total += this->pennies * 0.01;
        return( total );
    }
};
