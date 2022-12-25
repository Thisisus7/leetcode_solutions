'''
Time: O(1) (32 bits) - constant
Space: O(1)
'''

class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = (n >> i) & 1  # (the last num of n) & 1 
            res = res | (bit << (31 - i))

        return res
