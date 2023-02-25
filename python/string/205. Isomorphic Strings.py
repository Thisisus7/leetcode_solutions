'''
2 Hash maps 
Time: O(n)
Space: O(N)
'''
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:        
        hashST, hashTS = {}, {}

        for i in range(len(s)):  # for c1, c2 in zip(s, t):
            if ((s[i] in hashST and hashST[s[i]] != t[i]) or 
                (t[i] in hashTS and hashTS[t[i]] != s[i])):
                return False

            hashST[s[i]] = t[i]
            hashTS[t[i]] = s[i]

        return True