'''
own
Time: O(n)
Space: O(1)
'''

class Solution:
    # own
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0

        for i in range(len(columnTitle)):
            digit = len(columnTitle) - 1 - i  # 0 ~ len(columnTitle) 
            val = ord(columnTitle[i]) - 64  # 1 ~ 26

            tempRes = 26 ** digit * val if digit > 0 else val

            res += tempRes

        return res