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
 * @return {number[]}
 */
// Recursive
var inorderTraversal = function(root) {
    const res = [];

    inorder = (root) => {
        if (!root) return;

        inorder(root.left);
        res.push(root.val);
        inorder(root.right);
    };
    inorder(root);
    return res;
};

// Iterative
var inorderTraversal = function(root) {
    const res = [];
    const stack = [];
    let cur = root;

    while(cur || stack.length) {  // stack.length not stack
        while (cur) {
            stack.push(cur);
            cur = cur.left;
        }
        cur = stack.pop();
        res.push(cur.val);
        cur = cur.right;
    }
    return res;
};