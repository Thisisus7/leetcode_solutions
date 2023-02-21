/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */

/**
 * @param {TreeNode} root
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {TreeNode}
 */

// Iteration
var lowestCommonAncestor = function(root, p, q) {
    let cur = root;

    while (cur) {
        if (p.val > cur.val && q.val > cur.val) cur = cur.right;
        else if (p.val < cur.val && q.val < cur.val) cur = cur.left;
        else return cur;
    }
};
// Recursion
var lowestCommonAncestor = function(root, p, q) {
    if (p.val > root.val && q.val > root.val) return lowestCommonAncestor(root.right, p, q);
    else if (p.val < root.val && q.val < root.val) return lowestCommonAncestor(root.left, p, q);
    else return root;
};