/**
 * @param {string[]} tokens
 * @return {number}
 */
var evalRPN = function(tokens) {
    const stack = [];
    for (let o of tokens) {
        switch (o) {
            case '+':
                stack.push(stack.pop() + stack.pop());
                break;
            case '*':
                stack.push(stack.pop() * stack.pop());
                break;
            case '-':
                let num2= stack.pop(), num1 = stack.pop();
                stack.push(num1 - num2);
                break;
            case '/':
                let n2 = stack.pop(), n1 = stack.pop();
                stack.push(n1 / n2 > 0 ? Math.floor(n1 / n2) : Math.ceil(n1 / n2));
                break;
            default:
                stack.push(Number(o));
        }
    }
    return stack[0];
};