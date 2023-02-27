/**
 * @param {number} n
 * @return {number}
 */
var arrangeCoins = function(n) {
    let l = 1, r = n;
    let res = 0;

    while (l <= r) {
        let mid = l + Math.floor((r - l) / 2);
        let coins = (mid + 1 ) * mid / 2;
        if (coins > n) {
            r = mid - 1;
        } else {
            l = mid + 1;
            res = Math.max(res, mid);
        } ;
    };
    return res;
};