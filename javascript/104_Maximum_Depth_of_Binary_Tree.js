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
 * @return {number}
 */


// Recursive DFS
var maxDepth = function(root) {
    if (!root) return 0;  // base case

    return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
};
// Iterative DFS
var maxDepth = function(root) {
    const stack = [[root, 1]];
    let res = 0;

    while (stack.length) {
        let [node, depth] = stack.pop();

        if (node) {
            res = Math.max(res, depth);
            stack.push([node.left, depth+1]);
            stack.push([node.right, depth+1]);
        }
    }
    return res;
};
// Iterative BFS
var maxDepth = function(root) {
    if (!root) return 0;

    const q = [root];
    let level = 0;

    while (q.length) {  // q.length, not q !!
        for (let i=q.length; i>0; i--) {  // for (let i=0; i<q.length; i++) won't work: don't know why for now
            const node = q.shift();  // must inside the for loop
            if (node.left) q.push(node.left);
            if (node.right) q.push(node.right);
        }
        level++;
    }
    return level;
};