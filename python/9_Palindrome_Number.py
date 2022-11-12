# 1
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        reverse_num = 0
        while x > reverse_num:
            reverse_num = 10 * reverse_num + (x % 10)
            x //= 10

        return x == reverse_num or x == reverse_num//10

output1 = Solution().isPalindrome(121)
output2 = Solution().isPalindrome(-121)
output3 = Solution().isPalindrome(10)

print(output1, output2, output3)

# 2
class Solution2:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        return s == s[::-1]  # str[<start>:<stop>:<step>]
