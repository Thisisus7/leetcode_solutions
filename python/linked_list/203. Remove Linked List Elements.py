'''
Two pointer (Iter)
Time: O(n)
Space: O(1 )
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Iter
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)  # new head
        prev = dummy  # prev: previous ptr
        while head:  # head: current ptr
            if head.val == val:
                prev.next = head.next
            else:
                prev = head
            head = head.next
        return dummy.next
    
    # Recur
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head == None:
            return head
        
        head.next = self.removeElements(head.next, val)
        return head.next if head.val == val else head


