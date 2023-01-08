'''
(own)
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:  # = for edge case (len(nums) == 0)
            mid = (l + r) // 2  # in C++ or Java, (l + r) may cause overflow, a better way is in js code
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                return mid

        return -1    