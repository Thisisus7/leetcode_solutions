/**
 * @param {string} pattern
 * @param {string} s
 * @return {boolean}
 */
var wordPattern = function(pattern, s) {
    const words = s.split(" ");
    if (words.length != pattern.length) return false;

    const words2pattern = new Map(), pattern2words = new Map();
    for (let i=0; i<pattern.length; i++) {
        if (words2pattern.has(words[i]) && words2pattern.get(words[i]) != pattern[i]) return false;
        if (pattern2words.has(pattern[i]) && pattern2words.get(pattern[i]) != words[i]) return false;

        words2pattern.set(words[i], pattern[i]);
        pattern2words.set(pattern[i], words[i]);
    }
    return false;
};