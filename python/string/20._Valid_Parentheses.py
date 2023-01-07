'''
Key:
1. lost as many cases as possible 
2. in python: stack(list), hashmap(dict)
'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = {')': '(', ']': '[', '}': '{'}

        for c in s:
            if c in map:
                if stack and stack[-1] == map[c]:  # if stack is not empty, otherwise index may be out of range
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False


output1 = Solution().isValid("()")
output2 = Solution().isValid("()[]{}")
output3 = Solution().isValid("(]")
print(output1, output2, output3)