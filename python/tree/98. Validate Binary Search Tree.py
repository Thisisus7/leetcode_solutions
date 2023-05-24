'''
DFS
Time: O(n) -- 2n
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, left, right):
            if not node:   # Empty tree
                return True
            if not (left < node.val and node.val < right):  # left < node.val < right
                return False
            
            return (valid(node.left, left, node.val) and    # prev < node < parent
                    valid(node.right, node.val, right))     # parent < node < prev
        
        return valid(root, float("-inf"), float("inf"))     # -infinity < root < infinity 
    
    def isValidBST(self, root: Optional[TreeNode], left = float("-inf"), right = float("inf")) -> bool:
        if not root:   # Empty tree
            return True

        return (left < root.val < right and 
                self.isValidBST(root.left, left, root.val) and
                self.isValidBST(root.right, root.val, right))