# Problem: Best Time to Buy and Sell Stock (LeetCode #121)
# Given an array prices where prices[i] is the price of a stock on day i,
# return the maximum profit you can achieve from a single buy-sell transaction.
# Return 0 if no profit is possible.

# Approach: One Pass (Greedy)
# Time Complexity: O(n)
# Space Complexity: O(1)

def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        # update the minimum buying price seen so far
        if price < min_price:
            min_price = price
        # update the maximum profit if selling today beats current best
        elif price - min_price > max_profit:
            max_profit = price - min_price

    return max_profit


# driver code
prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))   # Output: 5  (buy at 1, sell at 6)

prices2 = [7, 6, 4, 3, 1]
print(maxProfit(prices2))  # Output: 0  (prices only decrease)
