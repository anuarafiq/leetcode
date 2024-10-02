class Solution(object):
    def maxProfit(self, prices):
        minimum = 99999
        profit = 0
        for price in prices:
            if price < minimum:
                minimum = price
            profit = max(profit, price - minimum)
      
        return profit