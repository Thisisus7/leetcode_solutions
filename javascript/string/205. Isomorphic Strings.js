/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isIsomorphic = function(s, t) {
    const mapST = new Map(), mapTS = new Map();  // can only use .indexOf()

    for (let i=0; i<s.length; i++) {
        if ((mapST.has(s[i]) && mapST.get(s[i]) != t[i]) ||
            (mapTS.has(t[i]) && mapST.get(t[i]) != s[i])) {
                return false;
            }

        mapST.set(s[i], t[i]);
        mapTS.set(t[i], s[i]);
    };
    return true;
};