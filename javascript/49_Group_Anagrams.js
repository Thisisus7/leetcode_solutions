/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    const res = new Map();

    for (let s of strs) {
        const count = new Array(26).fill(0);

        for (let c of s) {
            count[c.charCodeAt(0) - 'a'.charCodeAt(0)] ++;
        }
        res[count] ? res[count].push(s): res[count] =[s];  
    }
    return Object.values(res);
};