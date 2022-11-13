'''
Key:
1. Do not allocate extra space for another array
2. two pointers; 1 for input, 1 for output
'''

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1  # left pointer
        for r in range(1, len(nums)):  # right pointer, 1: the 1st number doesn't need any processing
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l += 1
        return l, nums

output1 = Solution().removeDuplicates([1, 1, 2])
output2 = Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4])
print(output1, output2)


            