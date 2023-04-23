'''
BackTracking:
Time: O(4^n)  -- 4: 'pqrs' or 'wxyz'
Space: O(4^n)
'''

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        keyboard = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def backTrack(i, curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            for c in keyboard[digits[i]]:  # each recursive call: 3~4 iters
                backTrack(i + 1, curStr + c)

        if digits:
            backTrack(0, "")

        return res