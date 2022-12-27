/**
 * @param {string} s
 * @return {boolean}
 */

// Solution 1
var isPalindrome = function(s) {
    let newStr = '';

    for (c of s) {
        if (/^[a-z0-9]+$/gi.test(c)) {  // g: global match; i: case-insensitive; $: end of string
            newStr += c;
        }
    }
    revStr = newStr.split('').reverse().join('');

    return newStr.toLowerCase() == revStr.toLowerCase();
};

// Solution 2
var isPalindrome2 = function(s) {
    s = s.replace(/[^a-zA-Z0-9]/g,"").toLowerCase();
    let l = 0, r = s.length - 1;

    while (l < r) {
        if (s[l] != s[r]) {
            return false
        };
        l++, r--;
    }
    return true;
};


output = isPalindrome2("A man, a plan, a canal: Panama");
console.log(output)