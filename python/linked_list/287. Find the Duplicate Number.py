'''
Floyd's Cycle Detection
Time: O(n)
Space: O(1)

Thank values as pointers
0 =p=> 1 ==> 2 ==> 3 ==> ==> 4 ==> 5 =x=> 1
c: cycle
2 * slow = fast 
2(p + c - x) = p + c - x + c
2p + 2c - 2x = p + 2c - x
p = x
'''

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = slow2 = 0
        while True:
            slow = nums[slow]  # x
            fast = nums[nums[fast]]  # 2x
            if slow == fast:
                break

        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow

