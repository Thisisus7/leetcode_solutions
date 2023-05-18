'''
Own
Time: O(2n)
Space: O(1)

More elegant
Time: O(n)
Space: O(1)
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:  # if only contain 1 code, return None
            return None

        prev, curr = None, head

        while curr:  # reverse
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        cnt = 1
        while prev:  # reverse again
            nxt = prev.next
            if n != cnt:  # if n == cnt, directly go to the next node: prev = prev.next
                prev.next = curr
                curr = prev
            prev = nxt
            cnt += 1

        return curr  # return head is wrong, because the 1st node may be removed
    
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        l = dummy
        r = head

        while n > 0 and r:
            r = r.next
            n -= 1
        
        while r:
            l, r = l.next, r.next

        l.next = l.next.next
        return dummy.next  # return head is wrong