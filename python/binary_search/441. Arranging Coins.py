'''
own
Time: O(n)
Space: O(1)
Binary search
Time: O(logn)
Space: O(1)
'''
class Solution:
    def arrangeCoins(self, n: int) -> int:
        minus = 1
        cnt = 0

        while n >= minus:
            n -= minus
            minus += 1
            cnt += 1

        return cnt
    
    def arrangeCoins(self, n: int) -> int:
        # Guass formula: (n+1)n/2
        l, r = 1, n
        res = 0

        while l <= r:
            mid = l + (r - l) // 2
            coins = (mid + 1) * mid / 2
            if coins > n:
                r = mid - 1
            else:
                l = mid + 1
                res = max(res, mid)

        return res