'''
Space 1: O(n)
Space 2: O(1)
'''

class Solution:
    # Solution 1
    def isPalindrome(self, s: str) -> bool:
        newStr = ''

        for c in s:
            if c.isalnum():
                newStr += c.lower()

        return newStr == newStr[::-1]   # start:stop:step 

    # Solution 2
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1  # left_pointer, right_pointer

        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while l < r and not self.alphaNum(s[r]):
                r -= 1
            
            if s[l].lower() != s[r].lower():
                return False
            
            l, r = l + 1, r - 1

        return True

    # Solution 3
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while l < r and not self.alphaNum(s[r]):
                r -= 1
            
            x, y = s[l], s[r]

            if ord('A') <= ord(x) <= ord('Z'):
                x = chr(ord(x) + 32)
            if ord('A') <= ord(y) <= ord('Z'):
                y = chr(ord(y) + 32)

            if x != y:
                return False
            
            l, r = l + 1, r - 1

        return True

    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or 
                ord('0') <= ord(c) <= ord('9'))