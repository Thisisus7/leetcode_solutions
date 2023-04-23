/*
const gcd = (a, b) => (0 === b ? a : gcd(b, a % b)):
1. If b is zero, then the function returns a because the GCD of a and 0 is a.
2. If b is not zero, the function recursively calls itself with b as the new value 
    of a and the remainder of a divided by b as the new value of b. This is because 
    the GCD of two numbers a and b is the same as the GCD of b and a % b, where % 
    is the modulo operator that returns the remainder of a division.
3. The recursive calls continue until b becomes zero, at which point the function 
    returns the value of a, which is the GCD of the original a and b.
*/

/**
 * @param {string} str1
 * @param {string} str2
 * @return {string}
 */
var gcdOfStrings = function(str1, str2) {
    const len1 = str1.length, len2 = str2.length;
    
    for (let i = Math.min(len1, len2); i > 0; i--) {
        if ((len1 % i == 0) && (len2 % i == 0)) {
            const subStr = str1.slice(0, i);
            if ((subStr.repeat(len1/i) === str1) && (subStr.repeat(len2/i) === str2)) {
                return subStr;
            }
        }
    }
    return "";
};

// gcd
var gcdOfStrings = function(str1, str2) {
    if (str1 + str2 !== str2 + str1) return '';

    const gcd = (a, b) => (0 === b ? a : gcd(b, a % b));
    return str1.substring(0, gcd(str1.length, str2.length));
};