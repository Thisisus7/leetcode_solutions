// Simulate .map(): Solve it without the built-in Array.map method.

/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    // return arr.map((val, idx) => {
    //     return fn(val, idx);
    // });
    const res = [];
    arr.forEach((val, idx) => {
        res.push(fn(val, idx));
    });
    return res;
};

// Input: arr = [1,2,3], fn = function plusI(n, i) { return n + i; }
// Output: [1,3,5]