/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
    let rob1= 0, rob2 = 0

    for (n of nums) {
        temp = Math.max(rob1 + n, rob2);
        rob1 = rob2;
        rob2 = temp;
    }
    return rob2;
};