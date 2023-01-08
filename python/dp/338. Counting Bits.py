'''
(own)
Time: O(n * len(bin(n)))
Space: O(n)
dp
Time:O(n)
Space: O(n)
'''

class Solution:
    # own
    def countBits(self, n: int) -> List[int]:
        res = []
        cnt = 0
        for i in range(n+1):
            for c in bin(i):
                if c == '1':
                    cnt += 1
            res.append(cnt)
            cnt = 0

        return res

    # dp
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n+1)
        offset = 1

        for i in range(1, n + 1):
            if offset * 2 == i:
                offset *= 2

            dp[i] = 1 + dp[i - offset]

        return dp

    # 0: 0 0 0 0  -- 0
    # 1: 0 0 0 1  -- 1 + dp[n - 1]
    # 2: 0 0 1 0  -- 1 + dp[n - 2]
    # 3: 0 0 1 1  -- 1 + dp[n - 2]
    # 4: 0 1 0 0  -- 1 + dp[n - 4]
    # 5: 0 1 0 1
    # 6: 0 1 1 0
    # 7: 0 1 1 1
    # 8: 1 0 0 0  -- 1 + dp[n - 8]
    # 9: 1 0 0 1  -- 1 + dp[n - 8]
