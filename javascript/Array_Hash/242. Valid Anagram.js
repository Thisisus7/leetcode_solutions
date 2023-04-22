/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    const hash = new Map();

    for (let w of s) {
        hash.set(w, (hash.get(w) || 0) + 1);
    }

    for (let w of t){
        if (!hash.has(w) || hash.get(w) === 0) return false;

        hash.set(w, hash.get(w) - 1);
        if (hash.get(w) == 0) hash.delete(w);
    }
    return hash.size <= 0;
};