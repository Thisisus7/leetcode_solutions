'''
deque (own)
Time: O(len(s) + len(t))
Space: O(len(s))
Two pointer:
Time: O(n)
Space: O(1)
'''

from collections import deque

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        q = deque([0] * len(s))

        for i, c in enumerate(s):
            q[i] = c

        for c in t:
            if not q:  # check q is not None
                return True
            if c == q[0]:
                q.popleft()


        return True if not q else False

    # two pointer
    def isSubsequence(self, s: str, t: str) -> bool:
        l, r = 0, 0

        while l < len(s) and r < len(t):
            if s[l] == t[r]:
                l += 1  # or s = s[1:]

            r += 1

        return True if l == len(s) else False  # or 0 == len(s) 
