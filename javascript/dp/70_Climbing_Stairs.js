/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function(n) {
    let one = 1, two = 1
    for (let i=0; i< n-1; i++) {
        temp = one;
        one += two;
        two = temp;
    }
    return one;
};

output1 = climbStairs(n = 2)  // 2
output2 = climbStairs(n = 3)  // 3
console.log(output1, output2)