// 1. Reverse String
var isPalindrome = function(x) {
    // 1) x is negative  2)x is at least two digits，the single digit of x is 0
    if (x < 0 || (x % 10 === 0 && x !== 0)) {
        return false;
    }
    let s = String(x);
    rs = '';
    for (let i = s.length-1; i>=0; i--) {
        rs += s[i];
    }
    return s === rs;
};

output1 = isPalindrome(121);
output2 = isPalindrome(-121);
output3 = isPalindrome(10);
console.log(output1, output2, output3);

// 2.
var isPalindrome2 = function(x) {
    
}
