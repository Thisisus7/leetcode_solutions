'''
dp(dynamic programming) - bottom up - solve subproblems until solve real problems
greedy: not work
brute force: DFS(depth first search) - backtracking
'''
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp = [12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12]
        # dp[i]: how many coins we need if amount = i
        dp = [amount + 1] * (amount + 1)  # [amount + 1]: max value anyway
        dp[0] = 0  # if amount = 0, we need 0 coin 
        
        for a in range(1, amount+1):
            for c in coins:
                if a - c >= 0:
                    # min: compare default value and new value
                    # 1 + dp[a - c]: 1(current coin); dp[a-c]: previous coin
                    dp[a] = min(dp[a], 1 + dp[a - c])

        return dp[amount] if dp[amount] != amount+1 else -1


output1 = Solution().coinChange([1,2,5], 11)
output2 = Solution().coinChange([2], 3)
output3 = Solution().coinChange([1], 0)
print(output1, output2, output3)