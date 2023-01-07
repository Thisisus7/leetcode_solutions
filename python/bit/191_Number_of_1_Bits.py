'''
Solution 1:
Time: O(len(n)) = O(1) (according to question (32 bits))
Space: O(1)
Solution 2 (better):
Time: O(# of 1s) = O(1)
Space: O(1)
'''

class Solution:
    # Solution 1
    def hammingWeight(self, n: int) -> int:
        res = 0

        while n:
            res += n % 2  # n & 1
            n = n >> 1  # n /= 2

        return res

    # Solution 2: for each step, get rid of a '1', and count 1 (draw some examples)
    def hammingWeight(self, n: int) -> int:
        res = 0

        while n:
            n &= (n - 1)
            res += 1

        return res
