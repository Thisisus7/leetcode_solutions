'''
Binary search
O(logn)
'''

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1  # 2 pointers

        while l <= r:
            mid = (l + r) // 2  # move mid pointer automatically
            if target == nums[mid]:
                return mid
            if target > nums[mid]:
                l = mid + 1
            else:  # target < nums[mid]
                r = mid -1

        return l  # really important


output1 = Solution().searchInsert(nums = [1,3,5,6], target = 5)
output2 = Solution().searchInsert(nums = [1,3,5,6], target = 2)
output3 = Solution().searchInsert(nums = [1,3,5,6], target = 7)
print(output1, output2, output3)