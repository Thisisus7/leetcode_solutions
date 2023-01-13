'''
hashmap (own):
Time: O(n)
Space: O(n)
Boyer_Moore: the majority element always exists in the array
Time: O(n)
Space: O(1)
'''

class Solution:
    # own
    def majorityElement(self, nums: List[int]) -> int:
        hash = {}

        for n in nums:
            hash[n] = 1 + hash.get(n, 0) 

            if hash[n] > len(nums) / 2:
                return n

    # also using hashmap
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        res, maxCount = 0, 0

        for n in nums:
            count[n] = 1 + count.get(n, 0)  # 0:  A value to return if the specified key does not exist.
            res = n if count[n] > maxCount else res
            maxCount = max(count[n], maxCount)

        return res

    # Space: O(1)
    def majorityElement(self, nums: List[int]) -> int:
        res, count = 0, 0

        for n in nums:
            if count == 0:
                res = n

            count += (1 if n == res else -1)

        return res