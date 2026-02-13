#include <iostream>
#include <string>
using namespace std;

int lengthOfLastWord(string s) {
    int n = s.length();
    int i = n - 1;
    int length = 0;

    // Step 1: Skip trailing spaces
    while (i >= 0 && s[i] == ' ') {
        i--;
    }

    // Step 2: Count characters of last word
    while (i >= 0 && s[i] != ' ') {
        length++;
        i--;
    }

    return length;
}

int main() {
    string s;
    getline(cin, s);  // to take full string input including spaces

    cout << lengthOfLastWord(s) << endl;

    return 0;
}
