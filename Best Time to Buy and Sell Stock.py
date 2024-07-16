121. Best Time to Buy and Sell Stock

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        
        return max_profit

# Example usage:
prices1 = [7, 1, 5, 3, 6, 4]
sol = Solution()
print(sol.maxProfit(prices1))  # Output: 5

prices2 = [7, 6, 4, 3, 1]
print(sol.maxProfit(prices2))  # Output: 0
