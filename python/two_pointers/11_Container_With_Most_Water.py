'''
Brute force:
Time: O(n^2)
2 pointers:
Time: O(n)
'''

class Solution:
    # Brute force: time limit exceeded
    def maxArea(self, height: List[int]) -> int:
        res = 0

        for l in range(len(height)):  # left pointer
            for r in range(l+1, len(height)):
                area = (r - l) * min(height[l], height[r])
                res = max(area, res)

        return res

    # 2 pointers (l always < r)
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0

        while l < r:
            area = min(height[l], height[r]) * (r - l)
            res = max(area, res)

            if height[l] < height[r]:
                l += 1
            else: 
                r -= 1

        return res