"""
121. Best Time to Buy and Sell Stock
@Level: Easy

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.
"""

class Solution:
    def maxProfit(self, prices):
        if prices is None or len(prices) <= 1:
            return 0
        buy = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] - buy > max_profit:
                max_profit = prices[i] - buy
            elif prices[i] < buy:
                buy = prices[i]
            else:
                pass
        return max_profit