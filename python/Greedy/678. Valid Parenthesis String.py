'''
brute force:
    TIme: O(3^n)
Cache:
    Time: O(n^3)
Greedy:
    Time: O(n)
    Space: O(1)
'''

class Solution:
    def checkValidString(self, s: str) -> bool:
        # leftMin <= number of '(' <= leftMax
        leftMin = leftMax = 0

        for c in s:
            if c == '(':
                leftMin, leftMax = leftMin + 1, leftMax + 1
            elif c == ')':
                leftMin, leftMax = leftMin - 1, leftMax - 1
            else:  # c == '*'
                leftMin, leftMax = leftMin - 1, leftMax + 1
            if leftMax < 0:
                return False
            if leftMin < 0:  # make leftMin in a right range
                leftMin = 0
        return leftMin == 0