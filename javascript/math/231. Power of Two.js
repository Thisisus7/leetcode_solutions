/**
 * @param {number} n
 * @return {boolean}
 */
var isPowerOfTwo = function(n) {
    if (n < 1) return false;
    if (n == 1) return true;
    
    return isPowerOfTwo(n / 2);
};

var isPowerOfTwo = function(n) {
    return n > 0 && ((n & n-1) === 0);
};