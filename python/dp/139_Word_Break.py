'''
brute force: 
1.check every single possible prefix: Time: O(n^2) 
2. check every single word in dict: Time: O(n * m * n)
DP:

'''
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:  # s="leetcode", wordDict=["leet", "code"]
        dp = [False] * (len(s) + 1)  # dp = [False, False, False, False, False, False, False, False, False]
        dp[len(s)] = True  # dp = [False, False, False, False, False, False, False, False, True]

        for i in range(len(s)-1, -1, -1):  # 7, 6, 5, 4, 3, 2, 1, 0
            for w in wordDict:  # "leet", "code"
                if (i + len(w) <= len(s)) and (s[i: i+len(w)] == w):  # s[4: 4+4] == "code"
                    dp[i] = dp[i + len(w)]  # [False, False, False, False, True, False, False, False, True]

                if dp[i]:  # if dp[i] is already true, we don't need to check other words in wordDict
                    break

        return dp[0]