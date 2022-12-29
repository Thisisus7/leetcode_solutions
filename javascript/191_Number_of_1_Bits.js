/**
 * @param {number} n - a positive integer
 * @return {number}
 */

// Solution 1
var hammingWeight = function(n) {
    let res = 0;

    while (n.length) {
        res += n % 2;
        n = n >>> 1;  // >>>: The high bit is filled with 0; >>: the high bit is filled with the sign bit
    }
    return res;
};
// Solution 2
var hammingWeight = function(n) {
    let res = 0;

    while (n) {
        res ++;
        n &= n - 1;
    }
    return res;
};