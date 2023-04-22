'''
Method1:
    1. if the array is sorted:
        if nums[l] < nums[r]: return nums[l]
    2. if the array is unsorted:
        if nums[m] >= nums[l]: search right
        else: search left

Method2:
    Compare nums[m] with nums[r]
    
Time: O(logn)
Space: O(1)

method3:
    min() -- TIme: O(n)
'''

class Solution:
    # method 1
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[0]

        while l <= r:
            if nums[l] <= nums[r]:
                res = min(res, nums[l])
                break
            
            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1

        return res

    # method2
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:  # if l == r: break
            m = (l + r) >> 1
            if nums[m] < nums[r]:
                r = m  # because nums[m] may be the minimum
            else:
                l = m + 1  # because nums[m] won't be the minimum

        return nums[l]  # or nums[r]