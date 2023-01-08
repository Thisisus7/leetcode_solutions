/**
 * @param {number} n
 * @return {number}
 */
var fib = function(n) {
    if (n <= 1) return n;

    let l = 0, r = 1;
    for (let i=2; i<n+1; i++) {
        const temp = r;
        r = r + l;
        l = temp;
    }
    return r;
};