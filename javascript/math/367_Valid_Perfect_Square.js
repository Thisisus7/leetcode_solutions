/**
 * @param {number} num
 * @return {boolean}
 */
var isPerfectSquare = function(num) {
    let l = 1, r = num;

    while (l <= r) {
        mid = l + Math.floor((r - l) / 2);
        if (mid * mid > num) r = mid - 1;
        else if (mid * mid < num) l = mid + 1;
        else return true;
    }
    return false;
};