/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    const hash = new Map();

    for (n of nums) {
        if (hash.has(n)) hash.set(n, hash.get(n)+1);
        else hash.set(n, 1);
        if (hash.get(n) > nums.length / 2) return n;
        console.log(hash);
    }
};

var majorityElement = function(nums) {
    let res = 0, count = 0;

    for (n of nums) {
        if (count == 0) res = n;

        res == n ? count++ : count--;
    }
    return res;
};