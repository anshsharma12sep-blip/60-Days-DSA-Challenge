#include <iostream>
#include <string>
using namespace std;

string reverseString(string s) {
    int left = 0;
    int right = s.length() - 1;

    while (left < right) {
        swap(s[left], s[right]);
        left++;
        right--;
    }

    return s;
}

int main() {
    string input;

    cout << "Enter a string: ";
    getline(cin, input);   // Allows spaces in input

    string reversed = reverseString(input);

    cout << "Reversed string: " << reversed << endl;

    return 0;
}
