'''
(own)
Time: O(n)
Space: O(1)
'''

class Solution:
    def tribonacci(self, n: int) -> int:
        l, m , r = 0, 1 ,1

        if n == 0: return l
        elif n == 1 or n == 2: return m

        for n in range(3, n+1):
            l, m, r = m, r, l + m + r

        return r