'''
Two pointer I:
Time: O(n)
Space: O(n)
Two pointer II:
Time: O(n)
Space: O(n)
Two pointer III (don't use [::-1]):
Time: O(n)
Space: O(1)
'''
class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                skipL, skipR = s[l+1 : r+1], s[l : r]
                return skipL == skipL[::-1] or skipR == skipR[::-1]

            l, r = l + 1, r - 1

        return True
    
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        isPalindrome = lambda x : x == x[::-1]

        while l < r:
            if s[l] != s[r]:
                return isPalindrome(s[l + 1 : r + 1]) or isPalindrome(s[l : r])
            
            l, r = l + 1, r - 1

        return True
    

