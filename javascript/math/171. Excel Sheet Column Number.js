/**
 * @param {string} columnTitle
 * @return {number}
 */
var titleToNumber = function(columnTitle) {
    let res = 0;
    let tempRes = 0;
    for (let i=0; i<columnTitle.length; i++) {
        let digit = columnTitle.length -1 - i;
        let val = columnTitle[i].charCodeAt(0) - 64;

        digit > 0 ? tempRes = 26 ** digit * val : tempRes = val;

        res += tempRes;
    }
    return res;
};