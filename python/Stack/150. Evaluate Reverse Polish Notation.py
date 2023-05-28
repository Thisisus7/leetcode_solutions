'''
Time: O(n)
Space: O(n)
'''

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for o in tokens:
            if o == '+':
                stack.append(stack.pop() + stack.pop())
            elif o == '*':
                stack.append(stack.pop() * stack.pop())
            elif o =='-':
                num2, num1 = stack.pop(), stack.pop()
                stack.append(num1 - num2)
            elif o == '/':
                num2, num1 = stack.pop(), stack.pop()
                stack.append(int(num1 / num2))
            else:
                stack.append(int(o))
        return stack[0]