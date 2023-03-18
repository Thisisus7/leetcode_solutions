/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isSymmetric = function(root) {
    var compare = (p, q) => {
        if (!p && !q) return true;
        if (!p || !q || p.val != q.val) return false;

        return compare(p.left, q.right) && compare(q.left, p.right); 
    }

    return compare(root.left, root.right);
};