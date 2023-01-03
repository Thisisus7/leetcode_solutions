'''
Time: O(logn)
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l ,r = 0, len(nums)-1

        while l <= r:  # =: for case like [x]
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid

            # if mid is in left portion
            if nums[l] <= nums[mid]:  # if len(nums) == 2, l = 0, r = 1, mid = 0, mid == l
                if (target <= nums[mid]) and (target >= nums[l]):
                    r = mid - 1
                else:
                    l = mid + 1
            # if mid is in right portion
            else:
                if (target >= nums[mid]) and (target <= nums[r]):
                    l = mid + 1
                else:
                    r = mid - 1

        return -1
