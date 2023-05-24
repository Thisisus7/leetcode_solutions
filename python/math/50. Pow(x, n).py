'''
Recursion
Time: O(log n)
Space: O(log n)

n is even: x^n = (x^2)^(n/2)
n is odd: x^n = x * (x^2)^((n-1)/2)
'''

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            if x == 0: return 0
            if n == 0: return 1

            res = helper(x * x, n // 2)
            return res * x if n % 2 else res
        
        res = helper(x, abs(n))
        return res if n >=0 else 1 / res