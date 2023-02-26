/**
 * @param {string[]} operations
 * @return {number}
 */
var calPoints = function(operations) {
    const stack = [];

    for (op of operations) {
        if (op == '+') stack.push(stack[stack.length - 2] + stack[stack.length - 1]);
        else if (op == 'D') stack.push(2 * stack[stack.length - 1]);
        else if (op == 'C') stack.pop();
        else stack.push(Number(op));
    }
    return stack.reduce((acc, cur) => acc + cur, 0);
};