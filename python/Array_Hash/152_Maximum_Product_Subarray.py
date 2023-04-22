'''
brute force: Time: O(n^2)
DP
Time: O(n)
Space: O(1)
'''

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)  # initial result
        curMax, curMin = 1, 1  # initial current max, current min. Because we have negative numbers

        for n in nums:
            # temp = curMax * n
            # curMax = max(curMax * n, curMin * n, n)
            # curMin = min(temp, curMin * n, n)
            curMax, curMin = max(curMax * n, curMin * n, n),  min(curMax * n, curMin * n, n)
            res = max(res, curMax)

        return res