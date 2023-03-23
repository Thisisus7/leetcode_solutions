'''
own (1 set)
Time: O(m + n)
Space: O(m + n)
'''

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        numSet = set(nums1)
        res = []

        for num in nums2:
            if num in numSet:
                res.append(num)
                numSet.remove(num)

        return res