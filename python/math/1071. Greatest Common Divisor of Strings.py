'''
Time: O(n)
Space: O(n)
'''

import math

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)
        for i in range(min(len1, len2), 0, -1):
            if (len1 % i == 0) and (len2 % i == 0):
                if (str1[:i] * (len1 // i) == str1) and (str1[:i] * (len2 // i) == str2):
                    return str1[:i]

        return ""
    
    # greatest common divisor 
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        
        return str1[:math.gcd(len(str1), len(str2))]