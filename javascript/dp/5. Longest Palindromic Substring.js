/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function(s) {
    let res = "";
    for (let i=0; i<s.length; i++) {
        for (let [l, r] of [[i, i], [i, i+1]]) {
            while (l >= 0 && r < s.length && s[l] === s[r]) {
                l--; r++;  // l can be -1
            }
            if (res.length < r - l - 1) res = s.slice(l+1, r);
        }
    }
    return res;
}