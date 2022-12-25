'''
Time: O(n)
Space: O(1)
'''
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1  # l (left) = buy; r (right) = sell
        max_profit = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
            else:
                l = r
            r += 1

        return max_profit


output1 = Solution().maxProfit(prices = [7,1,5,3,6,4])  # 5
output2 = Solution().maxProfit(prices = [7,6,4,3,1])  # 0
print(output1, output2)