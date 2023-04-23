'''
own; Two pointer:
Time: O(n)
Space: O(n)
'''

class Solution:
    # own
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        for i in range(min(len(word1), len(word2))):
            res += word1[i] + word2[i]

        for j in range(i, max(len(word1), len(word2))):
            res += word1[j] if (len(word1) > len(word2)) else word2[j]

        return res
    
    # Two pointer
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        i = j = 0
        len1, len2 = len(word1), len(word2)
        while i < len1 or j < len2:
            if i < len1:
                res += word1[i]
                i += 1
            if j < len2:
                res += word2[j]
                j += 1

        return res