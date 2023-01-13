'''
(own)
Time: O(n)
Space: O(n)
'''

class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0: return 0
        nums = [0, 1]

        for i in range(2, n+1):
            if i % 2 == 0:
                nums.append(nums[int(i/2)])
            else:
                nums.append(nums[int((i-1) / 2)] + nums[int((i-1) / 2 + 1)]) 

        return max(nums)