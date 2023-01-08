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
var isBalanced = function(root) {
    dfs = (root) => {
        if (!root) return [true, 0];

        const left = dfs(root.left), right = dfs(root.right);
        balanced = left && right && Math.abs(left[1] - right[1]) <= 1

        return [balanced, 1 + Math.max(left[1], right[1])];
    }
    return dfs(root)[0];
};