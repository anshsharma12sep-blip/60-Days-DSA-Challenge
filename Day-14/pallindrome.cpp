#include <iostream>
using namespace std;
int main() {
    int x;

    cout << "Enter an integer: ";
    cin >> x;
    if (x < 0) 
        cout<<"not pallindrome\n";

    int original = x;
    long long reversed = 0;  

    while (x > 0) {
        int digit = x % 10;
        reversed = reversed * 10 + digit;
        x /= 10;
    }
    if(original == reversed){
        cout<<"pallindrome number\n";
    }
    else{
        cout<<"not pallindrome number \n";
    }
}
