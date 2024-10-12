class Solution(object):
    def maxProfit(self, prices):
        profit = 0
        buy, sell = prices[0], 0
        n = len(prices)
        i = 0

        while i < n-1:
            while i < n-1 and prices[i] >= prices[i+1]:
                i += 1
            buy = prices[i]
            while i < n-1 and prices[i] <= prices[i+1]:
                i += 1
            sell = prices[i]
            profit += sell - buy
            i += 1

        return profit