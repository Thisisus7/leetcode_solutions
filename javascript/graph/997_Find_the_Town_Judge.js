/**
 * @param {number} n
 * @param {number[][]} trust
 * @return {number}
 */
var findJudge = function(n, trust) {
    const count = new Array(n+1).fill(0);

    for ([i, j] of trust) {
        count[i] --;
        count[j] ++;
    }
    for (let i=1; i<n+1; i++) {
        if (count[i] == n - 1)  return i;
    }
    return -1;
};