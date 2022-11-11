from typing import List

# 1. loop
class Solution:
    # input: int_list, int; output: int_list
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # range(start, stop, step)
        for i in range(len(nums)):  
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []


output = Solution().twoSum(nums = [3,2,4], target = 6)
print(output)

# 2
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pass
