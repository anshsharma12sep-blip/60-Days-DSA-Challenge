#include <iostream>
#include <unordered_map>
using namespace std;

bool isAnagram(string s1, string s2) {
    if (s1.length() != s2.length())
        return false;

    unordered_map<char, int> freq;

    // Count characters of first string
    for (char c : s1) {
        freq[c]++;
    }

    // Subtract using second string
    for (char c : s2) {
        freq[c]--;
        if (freq[c] < 0)  // Early exit optimization
            return false;
    }

    return true;
}

int main() {
    cout << isAnagram("listen", "silent") << endl; // 1 (True)
    cout << isAnagram("hello", "world") << endl;   // 0 (False)
}
