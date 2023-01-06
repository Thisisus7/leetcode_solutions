/**
 * @param {string} a
 * @param {string} b
 * @return {string}
 */
 var addBinary = function(a, b) {
    let res = "";
    let carry = 0;
    const aRev = a.split("").reverse().join(""), bRev = b.split("").reverse().join("")

    for (let i=0; i<Math.max(a.length, b.length); i++) {
        i < a.length ?  digitA = aRev[i].charCodeAt(0) - '0'.charCodeAt(0) : digitA = 0;
        i < b.length ?  digitB= bRev[i].charCodeAt(0) - '0'.charCodeAt(0) : digitB = 0;

        const total = digitA + digitB + carry;
        const char = (total % 2).toString();
        res = char + res;
        carry = Math.floor(total / 2);
    }
    if (carry) res = '1' + res;

    return res;
};

