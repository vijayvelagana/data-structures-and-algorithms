#include<iostream>
using namespace std;

void patternOne(){
    /*
        ****
        ****
        ****
        ****
    */
    cout << "Pattern One - Enter the value of n: ";
    int n;
    cin >> n;
    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            cout << "*";
        }
        cout << endl;
    }
}

void patternTwo(){
    /*
        *
        **
        ***
        ****
        *****
    */
    cout << "Pattern Two - Enter the value of n: ";
    int n;
    cin >> n;
    for(int i=0; i<n; i++){
        for(int j=0; j<=i; j++){
            cout << "*";
        }
        cout << endl;
    }
}

void patternThree(){
    /*
        1
        12
        123
        1234
        12345
    */
    cout << "Pattern Three - Enter the value of n: ";
    int n;
    cin >> n;
    for(int i=1; i<=n; i++){
        for(int j=1; j<=i; j++){
            cout << j;
        }
        cout << endl;
    }
}

void patternFour(){
    /*
        1
        22
        333
        4444
        55555
    */
    cout << "Pattern Four - Enter the value of n: ";
    int n;
    cin >> n;
    for(int i=1; i<=n; i++){
        for(int j=1; j<=i; j++){
            cout << i;
        }
        cout << endl;
    }
}

void patternFive(){
    /*
        *****
        ****
        ***
        **
        *
    */
    cout << "Pattern Five - Enter the value of n: ";
    int n;
    cin >> n;
    for(int i=0; i<n; i++){
        for(int j=0; j<n-i; j++){
            cout << "*";
        }
        cout << endl;
    }
}

void patternSix(){
    /*
        12345
        1234
        123
        12
        1
    */
    cout << "Pattern Six - Enter the value of n: ";
    int n;
    cin >> n;
    for(int i=1; i<=n; i++){
        for(int j=1; j<=n-i+1; j++){
            cout << j;
        }
        cout << endl;
    }
}

void patternSeven(){
    /*
            *
           ***
          *****
         *******
        *********
    */
    cout << "Pattern Seven - Enter the value of n: ";
    int n;
    cin >> n;
    for(int i=0; i<n; i++){
        for(int j=0; j<2*n-1; j++){
            if(j>=n-1-i && j<=n-1+i){
                cout << "*";
            }
            else{
                cout << " ";
            }
        }
        cout << endl;
    }
}

void patternEight(){
    /*
        *********
         *******
          *****
           ***
            *
    */
    cout << "Pattern Eight - Enter the value of n: ";
    int n;
    cin >> n;
    for(int i=0; i<n; i++){
        for(int j=0; j<2*n-1; j++){
            if(j>=i && j<=2*n-2-i){
                cout << "*";
            }
            else{
                cout << " ";
            }
        }
        cout << endl;
    }
}

void patternNine(){
    /*
            *
           ***
          *****
         *******
        *********
        *********
         *******
          *****
           ***
            *
    */
    // combination to previous two patterns
    cout << "Pattern Nine - Enter the value of n: ";
    int n;
    cin >> n;
    for(int i=0; i<2*n; i++){
        for(int j=0; j<2*n-1; j++){
            if(i<n && j>=n-1-i && j<=n-1+i){
                cout << "*";
            }
            else if(i>=n && j>=i-n && j<=2*n-2-i+n){
                cout << "*";
            }
            else{
                cout << " ";
            }
        }
        cout << endl;
    }
}

void patternTen(){
    /*
        *
        **
        ***
        ****
        *****
        *****
        ****
        ***
        **
        *
    */
    cout << "Pattern Ten - Enter the value of n: ";
    int n;
    cin >> n;
    for(int i=0; i<2*n; i++){
        for(int j=0; j<n; j++){
            if(i<n && j<=i){
                cout << "*";
            }
            else if(i>=n && j<=2*n-1-i){
                cout << "*";
            }
            else{
                cout << " ";
            }
        }
        cout << endl;
    }
}

int main(){
    patternOne();
    patternTwo();
    patternThree();
    patternFour();
    patternFive();
    patternSix();
    patternSeven();
    patternEight();
    patternNine();
    patternTen();
    
    return 0;
}

