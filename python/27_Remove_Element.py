from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        for r in range(len(nums)):
            if nums[r] != val:
                nums[l] = nums[r]
                l += 1
        
        return l

out1 = Solution().removeElement(nums = [3,2,2,3], val = 3)
out2 = Solution().removeElement(nums = [0,1,2,2,3,0,4,2], val = 2)
print(out1, out2)
