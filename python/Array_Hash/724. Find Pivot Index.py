'''
own
Time: O(n^2)

Time: O(n)
'''

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if sum(nums[0:i]) == sum(nums[i+1:]):
                return i
            
        return -1
    
    def pivotIndex(self, nums: List[int]) -> int:
        Total = sum(nums)  # O(n)
        leftSum = 0

        for i in range(len(nums)):
            RightSum = Total - leftSum - nums[i]
            if leftSum == RightSum:
                return i
            leftSum += nums[i]

        return -1
    
    def pivotIndex(self, nums: List[int]) -> int:
        l, r = 0, sum(nums)
        for i in range(len(nums)):
            r -= nums[i]
            if l == r:
                return i
            l += nums[i]

        return -1
