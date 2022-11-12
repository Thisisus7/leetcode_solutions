class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        res = 0 # result
        
        for i in range(len(s)):
            # check we don't go out of bound   check if s[i] < s[i+1]
            if i + 1 < len(s) and roman[s[i]] < roman[s[i+1]]:
                res -= roman[s[i]]  # if s[i] < s[i+1], then s[i] should be negative
            else:
                res += roman[s[i]]  # else s[i] is positive
        
        return res

output1 = Solution().romanToInt("LVIII")
output2 = Solution().romanToInt("MCMXCIV")
print(output1, output2)