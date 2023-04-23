/**
 * @param {string} word1
 * @param {string} word2
 * @return {string}
 */

// own (modified)
var mergeAlternately = function(word1, word2) {
    let res = "";

    for (let i=0; i < Math.max(word1.length, word2.length); i++) {
        if (i < word1.length) res += word1[i];
        if (i < word2.length) res += word2[i];
    }
    return res;
};

// Two pointer
var mergeAlternately = function(word1, word2) {
    let len1 = word1.length, len2 = word2.length;
    let i = j = 0;
    let res = "";

    while (i < len1 || j < len2) {
        if (i < len1) {
            res += word1[i];
            i++;
        }
        if (j < len2) {
            res += word2[j];
            j++;
        }
    }
    return res;
};