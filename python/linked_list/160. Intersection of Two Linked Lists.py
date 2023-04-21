'''
Two pointer
ptr1: headA => headB
ptr2: headB => headA
Time: O(m + n)
Space: O(1)
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        ptr1, ptr2 = headA, headB

        while ptr1 != ptr2:
            ptr1 = ptr1.next if ptr1 else headB
            ptr2 = ptr2.next if ptr2 else headA

        return ptr1