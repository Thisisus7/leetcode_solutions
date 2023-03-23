'''
own
Time O(n)
Space: O(1)
elegant way
Time: O(n)
Space: O(n)
'''

class Solution:
    def countSegments(self, s: str) -> int:
        if len(s) == 0:
            return 0

        count = 0
        for i in range(1, len(s)):
            if s[i] == " " and s[i-1] != " ":
                count += 1
        
        return count + 1 if s[-1] != " " else count
    
    def countSegments(self, s: str) -> int:
        return len(s.split())