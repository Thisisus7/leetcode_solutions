'''
1. two pointer (own)
Time: O(n)
Space: O(1)
2. s.reverse()
Time: O(n)
Space: O(1)
3. stack
Time: O(n)
Space: O(n)
'''

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l, r = 0, len(s) - 1

        while l < r:
            s[l], s[r] = s[r], s[l]

            l += 1
            r -= 1