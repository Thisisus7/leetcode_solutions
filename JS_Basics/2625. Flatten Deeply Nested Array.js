// Simulate Array.flat():
//      1. Recursion + forEach()
//      2. Recursion + reduce()
//      3. concat(): time limit exceeded
/**
 * @param {any[]} arr
 * @param {number} depth
 * @return {any[]}
 */

// Method 1
var flat = function (arr, n) {
    const res = [];
    arr.forEach((x) => {
        Array.isArray(x) && n > 0 
            ? res.push(...flat(x, n-1))  // => ...res
            : res.push(x);
    });
    return res;
};

// Method 2
var flat = function (arr, n) {
    return arr.reduce((accum, curr) => {
        Array.isArray(curr) && n > 0 
            ? accum.push(...flat(curr, n - 1))
            : accum.push(curr);
        
        return accum;
    }, []);
};

// Input
// arr = [1, 2, 3, [4, 5, 6], [7, 8, [9, 10, 11], 12], [13, 14, 15]]
// n = 1
// Output
// [1, 2, 3, 4, 5, 6, 7, 8, [9, 10, 11], 12, 13, 14, 15]