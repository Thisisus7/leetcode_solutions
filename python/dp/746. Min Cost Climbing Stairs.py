'''
DP (backward)
Time: O(n)
Space: O(1)
'''

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)  # set goal = 0

        for i in range(len(cost) - 3, -1, -1):  # e.g., 15 of [10, 15, 20, 0]
            cost[i] += min(cost[i + 1], cost[i + 2])  # current cost + later cost

        return min(cost[0], cost[1])