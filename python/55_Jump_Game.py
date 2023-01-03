'''
Brute force (DP/cache)
Time: O(n^2)
Greedy (goal -> start, look each number only once)
Time: O(n)
'''

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1  # index

        for i in range(len(nums)-1, -1, -1):  # len(nums)-1 to 0
            if i + nums[i] >= goal:  # i: current index; nums[i]: max steps
                goal = i

        return True if goal == 0 else False