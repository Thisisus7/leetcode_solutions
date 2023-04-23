/**
 * @param {string} s
 * @return {boolean}
 */
var validPalindrome = function(s) {
    let l = 0, r = s.length - 1;

    while (l < r) {
        if (s[l] != s[r]) {
            const skipL = s.slice(l);
            const skipR = s.slice(l, r);
            const skipLRev = skipL.split("").reverse().join("");
            const skipRRev = skipR.split("").reverse().join("");
            return skipL == skipLRev || skipR == skipRRev; 
        }
        l++;
        r--;
    }
    return true;
};
// better
var validPalindrome = function(s) {
    let l = 0, r = s.length - 1;

    const isPalindrome = (i, j) =>{
        for (; i<j; i++, j--) {
            if (s[i] != s[j]) return false;
        }
        return true;
    }

    for (; l<r; l++, r--) {
        if (s[l] != s[r]) return isPalindrome(l+1, r) || isPalindrome(l, r-1);
    }
    return true;
}