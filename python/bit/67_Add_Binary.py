'''
Time: O(n)
'''

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        carry = 0
        a, b = a[::-1], b[::-1]  # reverse a and b

        for i in range(max(len(a), len(b))):  # a and b may have different length
            digitA = ord(a[i]) - ord('0') if i < len(a) else 0  # convert str to int
            digitB = ord(b[i]) - ord('0') if i < len(b) else 0

            total = digitA + digitB + carry
            char = str(total % 2)
            res = char + res  # (res + char) is wrong
            carry = total // 2  # total = 2 or 3, carry = 1; total = 1, carry = 0

        if carry:  # if carry != 0
            res = '1' + res
            
        return res 



        



