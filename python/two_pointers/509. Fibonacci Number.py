'''
iterative (two pointer) (own)
Time: O(n)
Space: O(1)
'''

class Solution:
    # iterative
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        l, r = 0, 1
        for i in range(2, n+1):
            l ,r = r, l + r

        return r

    # recursion (bad)
    def fib(self, n: int) -> int:
        if n <= 1: return n

        return self.fib(n-2) + self.fib(n-1)