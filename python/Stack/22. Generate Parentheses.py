'''
BackTracking
if openNum == closedNum == n: add stack to res
if openNum < n: add '(' to stack
if openNum > closedNum: add ')' to stack
'''

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def backTrack(openNum, closedNum):
            if openNum == closedNum == n:
                res.append("".join(stack))
                return

            if openNum < n:
                stack.append('(')
                backTrack(openNum + 1, closedNum)
                stack.pop()

            if openNum > closedNum:
                stack.append(')')
                backTrack(openNum, closedNum + 1)
                stack.pop()

        backTrack(0, 0)
        return res



# if n = 3:
# 1:
# ( ( ( ) ) )
# 2:
# ( ( ) ( ) )
# 3:
# ( ( ) ) ( )
# 4
# ( ( ) ) ( )
# 5
# ( ) ( ( ) )
# 6
# ( ) ( ) ( )