class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0 

        # [rob1, rob2, n, n+1, ...]
        for n in nums:
            temp = max(rob1 + n, rob2)  # new max
            rob1 = rob2  # previous max
            rob2 = temp

        return rob2  