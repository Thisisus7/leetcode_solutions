/**
 * @param {number} x
 * @return {number}
 */
var mySqrt = function(x) {
    let l = 0, r = Math.floor(x / 2) + 1;
    let res = 0;

    while(l <= r) {
        let mid = Math.floor((l + r) / 2);
        if (mid * mid <= x) {
            res = mid;
            l = mid + 1;
        } 
        else r = mid - 1;
    }
    return res;  
};