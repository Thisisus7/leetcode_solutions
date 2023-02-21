'''
brute force: O(n^2)
Greedy
Time: O(n)
Space: O(1)
'''

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):  # no solution
            return -1
        
        total = 0
        res = 0  # start position
        for i in range(len(gas)):
            total += (gas[i] - cost[i])

            #  if total[0~i] < 0, and we know gas[0] - cost[0] >= 0, so total[1~i] always < 0
            if total < 0:
                res = i + 1 
                total = 0

        return res
