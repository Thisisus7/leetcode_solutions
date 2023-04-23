'''
dynamic programming
dp[i] = max(dp[i-k+1], dp[i-1]) + current_num 
bad method (basic dp): O(n^2)
middle method (priority queue): O(nlogn)
good method (monotonic queue): O(n)
deque: a kind of monotonic queue, O(1): append and pop
list: O(n): append and pop
'''
from typing import List

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        dp = [-10000] * len(nums)  # the max score when you are at ith position 
        dp[0] = nums[0]  # the score of the ist position
        window = [0]  # window = [the idx which maximizes dp[i]]

        for i in range(1, len(nums)):
            if window[0] == i - (k+1):  # i-3 can't exist in the window
                window.pop(0)
            
            dp[i] = nums[i] + dp[window[0]]  # dp[window[0]]: the biggest dp value for now

            while window and dp[window[-1]] <= dp[i]:
                window.pop()

            window.append(i)

        return dp[-1]

output1 = Solution().maxResult(nums = [1,-1,-2,4,-7,3], k = 2) 
output2 = Solution().maxResult(nums = [10,-5,-2,4,0,3], k = 3) 
output3 = Solution().maxResult(nums = [1,-5,-20,4,-1,3,-6,-3], k = 2) 
print(output1, output2, output3)

