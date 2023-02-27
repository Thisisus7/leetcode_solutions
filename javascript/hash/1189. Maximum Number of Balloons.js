/**
 * @param {string} text
 * @return {number}
 */
var maxNumberOfBalloons = function(text) {
    const counts = new Map(
        [
            ['b', 0],
            ['a', 0],
            ['l', 0],
            ['o', 0],
            ['n', 0],
        ]
    );
    for (let c of text) {
        if (counts.has(c)) {
            if (c == 'b' || c == 'a' || c == 'n') counts.set(c, counts.get(c) + 2);
            else if (c == 'l' || c =='o') counts.set(c, counts.get(c) + 1);
        };
    };
    return Math.floor(Math.min(...counts.values()));
};

var maxNumberOfBalloons = function(text) {
    const counts = {};

    for (let c of text) {
        counts[c] = (counts[c] || 0) + 1;
    };
    return Math.min(counts['b'], counts['a'], Math.floor(counts['l'] / 2), Math.floor(counts['o'] / 2), counts['n']) || 0;
}