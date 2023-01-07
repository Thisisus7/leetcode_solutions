'''
hashmap
O(n)
'''
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int: 
        res = 0  # result: num of subarrays
        curSum = 0  # current sum = 0: if the 1st value = k
        prefixSums = { 0 : 1 }  # add a 0 element at the left

        for n in nums:
            curSum += n
            diff = curSum - k  # current sum - k

            res += prefixSums.get(diff, 0)  # if diff is in the prefixSums, res +1; else res +0  
            prefixSums[curSum] = 1 + prefixSums.get(curSum, 0)  # add to prefixSums: {curSum : 1 + prev count}

        return res

output1 = Solution().subarraySum([1, 1, 1], 2)
output2 = Solution().subarraySum([1, 2, 3], 3)
print(output1, output2)