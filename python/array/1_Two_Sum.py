'''
Key:
1. using a hashmap to store numbers, and compare complements with numbers in hashmap
2. Reversing index and value, because of map.get() 
'''

from typing import List

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

