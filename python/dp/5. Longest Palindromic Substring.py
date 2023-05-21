'''
Center Diffusion
Time: O(n^2)
Space: O(1)
'''

class Solution:
    # Center Diffusion
    def longestPalindrome(self, s: str) -> str:
        resLen = 0
        resIdx = [-1, -1]
        def centerDiffusion(l, r, resLen, resIdx):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if resLen < r - l + 1:
                    resIdx[0], resIdx[1] = l, r + 1
                    resLen = r - l + 1
                l -= 1
                r += 1
            return resLen, resIdx

        for i in range(len(s)):
            resLen, resIdx = centerDiffusion(i, i, resLen, resIdx)      # odd length
            resLen, resIdx = centerDiffusion(i, i + 1, resLen, resIdx)  # even length
        
        return s[resIdx[0]: resIdx[1]]
    
    # Elegant Center Diffusion
    def longestPalindrome(self, s: str) -> str:
        res = ""

        for i in range(len(s)):
            for a, b in [(i, i), (i, i+1)]:
                while a >= 0 and b < len(s) and s[a] == s[b]:
                    a -= 1
                    b += 1
                if len(res) < b - a - 1:
                    res = s[a+1:b]

        return res
    