#include <iostream>
using namespace std;

int fib(int n) {
    if (n <= 1) return n;

    int prev2 = 0;   // F(0)
    int prev1 = 1;   // F(1)
    int current;

    for (int i = 2; i <= n; i++) {
        current = prev1 + prev2;
        prev2 = prev1;
        prev1 = current;
    }

    return prev1;
}

int main() {
    int n;
    cout << "Enter n: ";
    cin >> n;

    if (n < 0) {
        cout << "Invalid input. n must be non-negative." << endl;
        return 0;
    }

    cout << "Fibonacci number at position " << n << " is: " << fib(n) << endl;

    return 0;
}
