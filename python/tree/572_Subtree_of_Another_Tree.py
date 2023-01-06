'''
Time: O(len(root)*len(subRoot))
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: return True
        if not root: return False  # not root and subRoot
        if self.sameTree(root, subRoot): return True  # same tree?

        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))  # subtree?

    def sameTree(self, root, subRoot):
        if not root and not subRoot:  # same: root == subRoot == null
            return True
        
        if root and subRoot and root.val == subRoot.val:  # root and subRoot aren't null; 1st nodes are equal
            return (self.sameTree(root.left, subRoot.left) and  # check if left and right are equal 
                    self.sameTree(root.right, subRoot.right)) 

        return False  # 1 is empty, the other is not empty