'''
 play optimally: win  (list the situations)
 Time: O(1)
 Space: O(1)
'''

class Solution:
    def divisorGame(self, n: int) -> bool:
        return n % 2 == 0
