#include <iostream>
using namespace std;

int badVersion = 4; // Assume version 4 is the first bad version

// Simulated API
bool isBadVersion(int version) {
    return version >= badVersion;
}

int firstBadVersion(int n) {
    int low = 1;
    int high = n;

    while (low < high) {
        int mid = low + (high - low) / 2;

        if (isBadVersion(mid)) {
            high = mid; // first bad could be mid
        } else {
            low = mid + 1;
        }
    }

    return low;
}

int main() {
    int n = 10; // total versions
    int result = firstBadVersion(n);

    cout << "First Bad Version: " << result << endl;

    return 0;
}
