#include<iostream>
using namespace std;

int main(){
    int n;
    cin >> n;

    int c = 0;   // step counter

    while(n != 0){
        if(n % 2 == 0){
            n = n / 2;   // even case
        }
        else{
            n = n - 1;   // odd case
        }
        c++;   // count each step
    }

    cout << c;
}
