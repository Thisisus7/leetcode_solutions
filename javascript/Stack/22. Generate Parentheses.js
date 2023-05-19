/**
 * @param {number} n
 * @return {string[]}
 */
var generateParenthesis = function(n) {
    let res = [];
    let stack = "";

    const backTrack = (left, right) => {
        if (left === right && right === n) {
            res.push(stack);
            return;
        }
        if (left < n) {
            stack += '(';
            backTrack(left + 1, right);
            stack = stack.slice(0, -1);
        }
        if (left > right) {
            stack += ')';
            backTrack(left, right + 1);
            stack = stack.slice(0, -1);
        }
    }
    backTrack(0, 0);
    return res;
};