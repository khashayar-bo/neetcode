class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = 101
        best_profit = 0

        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            best_profit = max(profit, best_profit)

        return best_profit
                    
        

            