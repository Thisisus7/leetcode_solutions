'''
Key:
compare th 1st str with all the rest
'''
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs[0])):  # i in length of first string
            for s in strs:  # traverse 3 strings
                if i == len(s) or strs[0][i] != s[i]:  # if the string is run off, or not equal
                    return res
            res += strs[0][i]  # refresh result
        return res

output1 = Solution().longestCommonPrefix(["flower","flow","flight"])
output2 = Solution().longestCommonPrefix(["dog","racecar","car"])
print(output1, output2)