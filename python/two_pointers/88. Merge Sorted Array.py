'''
Time: O(n)
Space: O(1)
'''

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last = m + n - 1  # the last element of nums1

        while m > 0 and n > 0:  # index is m - 1, n - 1, so m and n should >= 1
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last] = nums1[m - 1]
                m -= 1
            else:
                nums1[last] = nums2[n - 1]
                n -= 1

            last -= 1 

        while n > 0:  # edge case: nums1 = [0], nums2 = [1]
            nums1[last] = nums2[n-1]
            n -= 1
            last -= 1

        return nums1