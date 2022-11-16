'''
Time: O(n)
Space: O(1)
'''

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i, cnt = len(s)-1, 0
        while s[i] == ' ':
            i -= 1
        while i >= 0 and s[i] != ' ':
            cnt += 1
            i -= 1
        
        return cnt


output1 = Solution().lengthOfLastWord("Hello World")
output2 = Solution().lengthOfLastWord("   fly me   to   the moon  ")
output3 = Solution().lengthOfLastWord("luffy is still joyboy")
print(output1, output2, output3)