#include <iostream>
using namespace std;

class Node
{
private:
    Node * next;
    string data;
public:
    //Constructor
    Node(string newData)
    {
        this->data = newData;
        this->next = NULL;
    }

    //Getters
    Node *GetNext(void)
    {
        return(this->next);
    }

    string GetData(void)
    {
        return(this->data);
    }

    //Setters
    void SetNext(Node *nextNode)
    {
        this->next = nextNode;
    }
    void SetData(string newData)
    {
        this->data = newData;
    }
};
class SinglyLinkedList {
private:
    Node * head;
public:
    //Constructors
    SinglyLinkedList(void) {
        this->head = NULL;
    }
    //Deconstructor
    ~ SinglyLinkedList(void) {
        Node *curNode = this->head;
        Node *nxtNode = this->head;
        // A node exists
        while(curNode != NULL) {
            //Get the next node in the list
            nxtNode = curNode->GetNext();
            // Delete the current node
            delete curNode;
            // Set current to next
            curNode = nxtNode;
        }

    }
    // Class Methods
    void push(string value) {
        Node * curNode = this->head;
        // Check to see if this is the first node to add
        if(this->head == NULL) {
            this->head = new Node(value);
        }
        else{
            // Search until the end
            while(curNode->GetNext() != NULL) {
                // Change to the next node
                curNode = curNode->GetNext();
            }
            // Found the end, add new node
            curNode->SetNext(new Node(value));
        }
    }
    void walk(void) {
        Node * curNode = this->head;
        while(curNode != NULL) {
            cout << curNode->GetData() << endl;
            curNode = curNode->GetNext();
        }
    }
    bool del(string value) {
        Node *curNode = this->head;
        Node *prvNode = this->head;
        // A node exists, search for a matching value
        while(curNode != NULL) {
            // Value matches, delete it!
            if(curNode->GetData() == value) {
                // Node is not the head node
                if(curNode != this->head) {
                    prvNode->SetNext(curNode->GetNext());
                    delete curNode;
                    curNode = prvNode;
                }
                // Node is the head node
                else{
                    this->head = curNode->GetNext();
                    delete curNode;
                    curNode = this->head;
                }
                return true;
            }
            // Advance to next node if not at end of the list
            if(curNode != NULL) {
                prvNode = curNode;
                curNode = curNode->GetNext();
            }
        }
        return false;
    }
};

int main(void)
{
    SinglyLinkedList test;
    test.push( "Mongoose" );
    test.push( "Kinkajou" );
    test.push( "Llama" );
    test.push( "Drama" );
    test.del( "Llama" );
    test.del( "Mongoose" );
    test.walk();
    return(0);
}