'''
own: Recursion
Time: O(n)
Space: O(1)
'''

class Solution:
    # own
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        if n < 1:
            return False

        return self.isPowerOfTwo(n / 2)
    

    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and ((n & n-1) == 0)