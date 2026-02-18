#include <iostream>
using namespace std;

int climbStairs(int n) {
    if (n <= 1) return 1;

    int prev2 = 1;  // ways(0)
    int prev1 = 1;  // ways(1)
    int current;

    for (int i = 2; i <= n; i++) {
        current = prev1 + prev2;
        prev2 = prev1;
        prev1 = current;
    }

    return prev1;
}

int main() {
    int n = 3;
    cout << climbStairs(n);
}
