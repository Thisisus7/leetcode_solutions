'''
brute force: Time: O(n^2)
bottom up:
Time: O(n)
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0  # remove nonlocal, let res = [0]

        def dfs(root):
            nonlocal res  # no nonlocal: Unbound error  
            if not root:
                return -1  # height of null node = -1

            left = dfs(root.left)
            right = dfs(root.right)
            res = max(res, left + right + 2)  # diameter = (left height + 1) + (right height + 1)
            
            return 1 + max(left, right)  # current height = 1 + max(left height, right height)

        dfs(root)
        return res
