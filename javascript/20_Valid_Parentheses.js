var isValid = function(s) {
    stack = [];
    map ={
        ')': '(',
        ']': '[',
        '}': '{'
    };

    for (c of s) {
        console.log(stack);
        if (c in map) {
            if (stack && stack[stack.length - 1] === map[c]) {
                stack.pop();
            } 
            else return false;
        } 
        else stack.push(c);
    }
    return !stack.length ? true : false;
};

output1 = isValid("()");
output2 = isValid("()[]{}");
output3 = isValid("(]");
console.log(output1, output2, output3);