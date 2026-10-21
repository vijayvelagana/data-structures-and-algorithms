#include<iostream>
using namespace std;

void patternEleven(){
    /*
        1
        01
        101
        0101
        10101
    */
    cout << "Pattern Eleven - Enter the value of n: ";
    int n;
    cin >> n;
    for(int i=0; i<n; i++){
        for(int j=0; j<=i; j++){
            if((i+j)%2 == 0){ // even
                cout << 1;
            }
            else{
                cout << 0;
            }
        }
        cout << endl;
    }
}

void patternTwelve(){
    /*
        1      1
        12    21
        123  321
        12344321
    */
    cout << "Pattern Thirteen - Enter the value of n: ";
    int n;
    cin >> n;
    for(int i=0; i<n; i++){
        for(int j=0; j<2*n; j++){
            if(j<n && j <= i){
                cout << j+1;
            }
            else if(j>=n && j>=(2*n-1-i)){
                cout << 2*n-j;
            }
            else{
                cout << " ";
            }
        }
        cout << endl;
    }
}

void patternThirteen(){
    /*
        1
        2 3
        4 5 6
        7 8 9 10
        11 12 13 14 15
    */
    
    // sigma (i+1) elements before (i+1) th row
    // sigma (i) before ith row
    // => i(i+1)/2 + (j+1) for value at pos(i,j)
    
    cout << "Pattern Fourteen - Enter the value of n: ";
    int n;
    cin >> n;
    for(int i=0; i<n; i++){
        for(int j=0; j<=i; j++){
            cout << (i*(i+1)/2) + (j+1);
            cout << " ";
        }
        cout << endl;
    }
}

void patternFourteen(){
    /*
        A
        AB
        ABC
        ABCD
        ABCDE
    */
    // toascii('A') is used to get ascii code of a char
    // char(65) is used to get char of an ascii code
    cout << "Pattern Fourteen - Enter the value of n: ";
    int n;
    cin >> n;
    for(int i=0; i<n; i++){
        for(int j=0; j<=i; j++){
            cout << char('A'+j);
        }
        cout << endl;
    }
}

void patternFifteen(){
    /*
        ABCDE
        ABCD
        ABC
        AB
        A
    */
    cout << "Pattern Fifteen - Enter the value of n: ";
    int n;
    cin >> n;
    for(int i=0; i<n; i++){
        for(int j=0; j<n-i; j++){
            cout << char('A'+j);
        }
        cout << endl;
    }
}

void patternSixteen(){
    /*
        A
        BB
        CCC
        DDDD
        EEEEE
    */
    cout << "Pattern Sixteen - Enter the value of n: ";
    int n;
    cin >> n;
    for(int i=0; i<n; i++){
        for(int j=0; j<=i; j++){
            cout << char('A'+i);
        }
        cout << endl;
    }
}

void patternSeventeen(){
    /*
           A
          ABA
         ABCBA
        ABCDCBA
    */
    cout << "Pattern Seventeen - Enter the value of n: ";
    int n;
    cin >> n;
    for(int i=0; i<n; i++){
        for(int j=0; j<2*n; j++){
            if(j<i && j>=n-1-i && j<=n-1+i){
                cout << char('A'+(i+j-n));
            }
            else if(j>=i && j>=n-1-i && j<=n-1+i){
                cout << char('A'+n-(j-1));
            }
            else{
                cout << " ";
            }
            j-(n-1)
        }
        cout << endl;
    }
}

int main(){
    // patternEleven();
    // patternTwelve();
    // patternThirteen();
    // patternFourteen();
    // patternFifteen();
    // patternSixteen();
    patternSeventeen();
    
    return 0;
}










