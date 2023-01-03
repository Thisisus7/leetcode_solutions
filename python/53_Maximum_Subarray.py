'''
brute force (3 loops): Time: O(n^3)
better(2 loops): Time: O(n^2)
best: 
Time: O(n)
Space: O(1)
'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]  # max subarray
        curSum = 0  # current sum

        for n in nums:
            if curSum < 0:  # if current sum < 0, clear current sum
                curSum = 0 

            curSum += n
            maxSub = max(curSum, maxSub)

        return maxSub
