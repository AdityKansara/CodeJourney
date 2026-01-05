# #121 - Best Time to Buy and Sell Stock
# Problem solved by Adity
# Time Complexity: O(n) - We iterate through the list once.
# Space Complexity: O(1) - Constant space used, no extra data structures.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        x = prices[0]  # Initialize the minimum price as the first price
        profit = 0  # Initialize profit as 0
        
        # Iterate through the list of prices
        for i in prices:
            # Update the minimum price if a lower price is found
            if i < x:
                x = i
            # Calculate the profit if selling at the current price and update the maximum profit
            profit = max(i - x, profit)
        
        return profit
