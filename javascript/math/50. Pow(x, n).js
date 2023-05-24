/**
 * @param {number} x
 * @param {number} n
 * @return {number}
 */
var myPow = function(x, n) {
    const helper = (x, n) => {
        if (x === 0) return 0;
        if (n === 0) return 1;

        res = helper(x * x, Math.floor(n / 2));
        return n % 2 ? res * x : res;
    }
    res = helper(x, Math.abs(n));
    return n >= 0 ? res : 1 / res;
};

var myPow = function (x, n) {
    if (n == 0) return 1;
    if (x == 0) return 0;
    if (n < 0) {
      n = -n;
      x = 1 / x;
    }

    let res = 1;
    while(n) {
      if (n & 1) res *= x;
      x *= x;
      n >>>= 1;
    }
    return res;
  };