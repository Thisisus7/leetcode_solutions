/**
 * @param {string} s
 * @return {boolean}
 */
var checkValidString = function(s) {
    let leftMin = 0, leftMax = 0;
    for (let c of s) {
        if (c === '(') {
            ++leftMax; ++leftMin;
        } else if (c === ')') {
            --leftMax; --leftMin;
        } else {
            ++leftMax; --leftMin;
        }
        if (leftMax < 0) return false;
        if (leftMin < 0) leftMin = 0; 
    }
    return leftMin === 0;
};