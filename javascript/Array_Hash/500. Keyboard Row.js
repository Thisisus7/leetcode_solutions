/**
 * @param {string[]} words
 * @return {string[]}
 */
var findWords = function(words) {
    const rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"];
    const res = [];
    let cnt = "";

    words.forEach(word => {
        for (let c of word) {
            rows.forEach((row, index) => {
                if (row.includes(c.toLowerCase())) { cnt += `${index}`; }
            }) 
        }
        if (new Set([...cnt]).size === 1) { res.push(word) };
        cnt = "";
    })
    return res;
};