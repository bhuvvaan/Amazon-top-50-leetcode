class Solution:
    def maxProfit(self, prices):

        if not prices or prices[0] is None:
            return 0
        min_sell_price = float('inf')
        max_profit = -float('inf')

        for i in prices:
            if i < min_sell_price:
                min_sell_price = i
            if i - min_sell_price > max_profit:
                max_profit = i - min_sell_price

        return max_profit
