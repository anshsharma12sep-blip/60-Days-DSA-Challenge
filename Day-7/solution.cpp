#include <iostream>
#include <vector>
using namespace std;

int maxProfit(vector<int>& prices) {
    if (prices.size() < 2)
        return 0;

    int minPrice = prices[0];
    int maxProfit = 0;

    for (int i = 1; i < prices.size(); i++) {
        // update profit if selling today is better
        maxProfit = max(maxProfit, prices[i] - minPrice);

        // update minimum buying price
        minPrice = min(minPrice, prices[i]);
    }

    return maxProfit;
}

int main() {
    vector<int> prices = {7, 1, 5, 3, 6, 4};
    cout << maxProfit(prices);
    return 0;
}
