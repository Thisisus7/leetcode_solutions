'''
Time: O(n)
'''
# use decision tree to understand this problem
# dp(bottom up): this problem -> fibonacci 
# e.g., n = 5 steps(0, 1, 2, 3 ,4 ,5): [8, 5, 3, 2, 1, 1]
class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        for i in range(n-1):  # compute n-1 times 
            temp = one
            one = one + two
            two = temp

        return one


output1 = Solution().climbStairs(n = 2)  # 2
output2 = Solution().climbStairs(n = 3)  # 3
print(output1, output2)