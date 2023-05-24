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
var isValidBST = function(root) {
    const valid = (node, left, right) => {
        if (!node) return true;
        if (!(left < node.val && node.val < right)) return false;

        return (valid(node.left, left, node.val) &&
                valid(node.right, node.val, right));
    }
    return valid(root, -Infinity, Infinity);
};

var isValidBST = function(root, left=-Infinity, right=Infinity) {
    if (!root) return true;

    return left < root.val && root.val < right &&
           isValidBST(root.left, left, root.val) &&
           isValidBST(root.right, root.val, right);
};