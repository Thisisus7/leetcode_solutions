/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isSubsequence = function(s, t) {
    let l = 0, r = 0;

    while(l < s.length && r < t.length) {
        if (s[l] == t[r]) l++;

        r++;
    }
    return l == s.length ? true : false;
};