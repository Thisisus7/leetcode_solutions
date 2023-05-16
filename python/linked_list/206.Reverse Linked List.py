'''
Iteration:
    Time: O(n)
    Space: O(1)
Recursion:
    Time: O(n)
    Space: O(n)
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Iteration
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            nxt = curr.next   # sava the path to next node
            curr.next = prev  # reverse
            prev = curr       # move to the next
            curr = nxt        # move to the next
        return prev           # return last

    # Recursion
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        newHead = self.reverseList(head.next)  # go to the last node, and reverse from back to front
        head.next.next = head                  # reverse
        head.next = None                       # current node points to None

        return newHead                         # always return the same node (last node)