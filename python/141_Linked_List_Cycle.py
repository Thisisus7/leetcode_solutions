'''
Time: O(n)
Space: O(1)
fast pointer: 2 steps; slow pointer: 1 step;
If this is a cycle, they'll always meet (slow pointer finish 1 cycle, fast pointer finish 2) 
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head  # initialization

        while fast and fast.next:  # fast and fast,next are not null
            slow = slow.next  # 1 step
            fast = fast.next.next  # 2 steps
            if slow == fast:
                return True

        return False