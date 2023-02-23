'''
Two pointer I:
Time: O(n)
Space: O(n)
Two pointer II:
Time: O(n)
Space: O(1)
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Two pointer I
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        nums = []
        # linked list to array
        while head:
            nums.append(head.val)
            head = head.next

        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] != nums[r]:
                return False
            l += 1
            r -= 1
        
        return True
    
    # Two pointer I
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Initialize two pointers
        fast, slow = head, head

        # move slow to the mid
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # Reverse second half
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        # Check palindrome
        l, r = head, prev
        while r:  # mid point is None
            if l.val != r.val:
                return False
            l = l.next
            r = r.next

        return True
