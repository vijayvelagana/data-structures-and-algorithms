#include<iostream>
using namespace std;

void modify(int &b){ // pass by reference i.e. address of the variable is passed
    cout << "value of b is " << b << endl;
    cout << "value of address of b is " << &b << endl;

    b = b + 10;
}

int main(){
    int a = 10;
    modify(a);
    cout << "value of a is " << a << endl;
    cout << "value of address of a is " << &a << endl;
    int *c = &a; // c is a pointer storing the address of variable a
    cout << "value of c is " << c << endl;
    cout << "value stored in the address stored by c is " << *c << endl;
    
    // & reference operator is used to get the address of a variable
    // * de-reference operator is used to find the value stored at an address

    int e = 100;
    int &d = e;
    cout << "value of d is " << d << endl;

    return 0;
}
