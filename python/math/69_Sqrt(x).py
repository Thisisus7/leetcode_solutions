'''
bad: Time: O(n), Space: O(1) 
binary search:
Time: O(logn)
Space: O(1)
'''

class Solution:
    # bad solution
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x

        for i in range(1, x//2 + 1):
            if i * i == x or (i+1) * (i+1) > x:  # i^2 = x or (i+1)^2 >x
                return i
    
    # binary search
    def mySqrt(self, x: int) -> int:
        l, r = 0, x // 2 + 1  # + 1 is necessary or just let r = x
        res = -1

        while l <= r:  # <= not <
            mid = (l + r) // 2

            if mid * mid <= x:
                res = mid
                l = mid + 1
            else:
                r = mid - 1

        return res