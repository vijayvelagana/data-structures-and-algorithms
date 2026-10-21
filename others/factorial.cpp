#include<bits/stdc++.h>
using namespace std;

class Solution{
    public:
    int findFactorial(int n){
        int res = 1;
        while(n){
            res *= n;
            n--;
        }
        return res;
    }
};

int main(){
    Solution obj;
    int n;
    cout << "Enter a number to find its factorial: ";
    cin >> n;
    cout << "Factorial of the number entered is: " << obj.findFactorial(n) << endl;
    return 0;

}
