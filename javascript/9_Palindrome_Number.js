/**
 * @param {number} x
 * @return {boolean}
 */

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
    if (x < 0 || (x % 10 === 0 && x !== 0)) {
        return false;
    }
    let reverse_num = 0;
    while(x > reverse_num) {
        reverse_num = reverse_num * 10 + (x % 10);  // r = 1, r = 12
        x = Math.floor(x / 10);  // x = 12, x = 1
    }
    return x === reverse_num || x === Math.floor(reverse_num / 10);  // x = 1, r = 12 , 1 = floor(12/10)
}

output4 = isPalindrome2(121);
output5 = isPalindrome2(-121);
output6 = isPalindrome2(10);
console.log(output4, output5, output6);
