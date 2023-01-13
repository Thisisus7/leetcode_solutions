/**
 * @param {number} n
 * @return {number}
 */
var tribonacci = function(n) {
    let l = 0, m = 1, r = 1;
    if (n == 0) return l;
    else if (n == 1 || n == 2) return m;

    for (let i=3; i<n+1; i++) {
        const temp = l;
        l = m;
        m = r;
        r = temp + l + m;  // l + n + r
    }
    return r;
};