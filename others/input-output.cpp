#include <iostream>
using namespace std;

int main(){
    cout << "Enter a number: ";
    int n;
    cin >> n;
    cin.ignore(); // cin >> leaves a new line char in the buffer and inorder to call getline function after cin >> called, clear the bugger as the getline function assumes \n as the end of the input and stops reading.
    cout << "The number you entered is: " << n << endl;
    
    cout << "Enter a string: ";
    string s;
    getline(cin, s);
    cout << "The string you entered is: " << s << endl;
    
    return 0;
}

