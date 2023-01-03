/**
 * // Definition for a Node.
 * function Node(val, neighbors) {
 *    this.val = val === undefined ? 0 : val;
 *    this.neighbors = neighbors === undefined ? [] : neighbors;
 * };
 */

/**
 * @param {Node} node
 * @return {Node}
 */
var cloneGraph = function(node) {
    const oldToNew = new Map();

    var dfs = function(node) {
        if (oldToNew.has(node.val))  return oldToNew.get(node.val);

        const copy = new Node(node.val);
        oldToNew.set(copy.val, copy);

        copy.neighbors = node.neighbors.map(nb => dfs(nb));

        return copy;
    }
    return node? dfs(node):null;
};