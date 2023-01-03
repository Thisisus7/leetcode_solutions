'''
Time: O(n)
Space: O(n)
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0  # l, r (left/right pointer): a sliding window: [l:r]
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[r])
                l += 1

            charSet.add(s[r])
            res = max(res, r-l+1)

        return res
