'''
Time: O(logn) -- height of the tre
Space: O(1)
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Iteration
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur = root  # current

        while cur:  # if cur != None
            if p.val < cur.val and q.val < cur.val:
                cur = cur.left    
            elif p.val > cur.val and q.val > cur.val:
                cur = cur.right
            else:
                return cur
            
    # Recursion   
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
            if p.val < root.val and q.val < root.val:
                return self.lowestCommonAncestor(root.left, p, q)   
            elif p.val > root.val and q.val > root.val:
                return self.lowestCommonAncestor(root.right, p, q)   
            else:
                return root
