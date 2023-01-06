'''
Key:
1. return the head
2. sort and merge
3. prehead and temp do not affect each other
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 1. Iteration
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        prehead = ListNode()  # ListNode(-1)
        temp = prehead

        while list1 and list2:
            if list1.val < list2.val:
                temp.next = list1
                list1 = list1.next  # list1
            else:
                temp.next = list2
                list2 = list2.next  # list2
            temp = temp.next  # output
        
        # if one of the list is ran out, then temp directly points to the other one
        temp.next = list1 if list1 else list2

        return prehead.next


# 2. Recursion
#  return order: l1(4) -> l2(4) -> l2(3) -> l1(2) -> l1(1) -> l2(1)
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        elif list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2

