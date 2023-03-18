'''
own
Time: O(n)
Space: O(1)
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Own
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def compare(p, q):
            if not p and not q:
                return True
            if (not p) or (not q) or (p.val != q.val):
                return False

            return compare(p.left, q.right) and compare(q.left, p.right)
        
        return compare(root.left, root.right)