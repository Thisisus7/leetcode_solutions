'''
inorder: left to right
Recursion:
Time: O(n)
Space: O(n)
Iterative:
Time: O(n)
Space: O(n)
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Recursion
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def inorder(root):
            if not root:
                return 
            
            # result depends on the order of these three lines 
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
            
        inorder(root)
        return res

    # Iterative
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        cur = root  # current pointer

        while cur or stack:
            while cur:  # in order: left to right
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right

        return res



