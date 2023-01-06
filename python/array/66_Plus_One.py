'''
Time: O(n)
Space: O(1)
handle 2 edges:
1. handle num of digits
2. handle 9
'''
from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]  # reverse the digits
        one = 1  # add one
        i = 0  # iters

        while one:  # one become a condition
            if i < len(digits):
                if digits[i] != 9:
                    digits[i] += 1
                    one = 0  # stop iters
                else:
                    digits[i] = 0  # 9 => 0
            else:
                digits.append(1)
                one = 0  # stop iters 
            i += 1  # update
            
        return digits[::-1]  # reverse digits back




output1 = Solution().plusOne([1, 2, 3])
output2 = Solution().plusOne([4, 3, 2, 1])
output3 = Solution().plusOne([9])
print(output1, output2, output3)