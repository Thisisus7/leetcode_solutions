'''
brute force: k = [ 1, 2, ... max(piles) ]
    Time: O(max(piles) * len(piles))
Binary Search:
    Time: O(log(max(piles)) * len(piles))
    Space: O(max(piles))
'''

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2

            hours = 0
            for p in piles:
                hours += math.ceil(p / k)

            if hours <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1

        return res