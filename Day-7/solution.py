from typing import List

def maxProfit(prices: List[int]) -> int:
    if len(prices) < 2:
        return 0

    min_price = prices[0]
    max_profit = 0

    for price in prices[1:]:
        # profit if we sell today
        max_profit = max(max_profit, price - min_price)

        # update minimum buying price
        min_price = min(min_price, price)

    return max_profit


# Example
prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))  # Output: 5
