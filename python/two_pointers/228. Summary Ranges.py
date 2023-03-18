class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []

        res = []
        l = r = 0
        while r < len(nums):
            if r < len(nums) - 1 and nums[r] + 1 == nums[r+1]:
                r += 1
            else:
                if nums[l] == nums[r]:
                    res.append(str(nums[l]))
                else:
                    res.append(str(nums[l]) + "->" + str(nums[r]))
                l = r = r + 1

        return res