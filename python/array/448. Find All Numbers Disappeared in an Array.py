'''
Time: O(n)
Space: O(1)

Time: O(n)
Space: O(n)
'''

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # if n is in nums, turn the value at index n into negative
        for n in nums:
            i = abs(n) - 1  # abs: if n has already been turned into negative
            nums[i] = -1 * abs(nums[i])

        # check
        res = []
        for i, n in enumerate(nums):
            if n < 0:
                res.append(i + 1)
        return res
    
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        return list(set(range(1,len(nums)+1)) - set(nums))
