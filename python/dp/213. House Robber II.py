'''
dp
Time: O(n)
Space: O(1)
'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        # nums[0] (edge case) : if len(nums) == 1
        return max(nums[0], self.houseRobberI(nums[1:]), self.houseRobberI(nums[:-1]))

    def houseRobberI(self, nums):
        rob1, rob2 = 0, 0
        for n in nums:
            rob1, rob2 = rob2, max(rob1 + n, rob2)

        return rob2