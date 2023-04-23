/**
 * @param {string} digits
 * @return {string[]}
 */
var letterCombinations = function(digits) {
    const res = [];
    const keyboard = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    };

    var backTrack = (i, curStr) => {
        if (digits.length == curStr.length) {
            res.push(curStr);
            return;
        }
        for (let c of keyboard[digits[i]]) backTrack(i + 1, curStr + c);
    }
    if (digits) backTrack(0, "");

    return res;   
};