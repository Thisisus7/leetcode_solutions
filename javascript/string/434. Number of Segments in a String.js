/**
 * @param {string} s
 * @return {number}
 */
// own
var countSegments = function(s) {
    if (s.length == 0) return 0;

    let count = 0;
    for (let i=1; i<s.length; i++) {
        if (s[i] == " " && s[i-1] != " ") count++;
    }
    return s[s.length-1] == " " ? count : count + 1;
};

// modification
var countSegments = function(s) {
    let count = 0;
    for (let i=0; i<s.length; i++) {
        if ((i == 0 || s[i-1] == " ") && s[i] != " ") count++;
    }
    return count;
};