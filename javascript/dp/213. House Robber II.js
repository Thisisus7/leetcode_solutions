/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
    return Math.max(nums[0], houseRobberI(nums.slice(1)), houseRobberI(nums.slice(0, -1)));
};

var houseRobberI = (nums) => {
    let rob1 = 0, rob2 = 0;
    for (n of nums) {
        newRob = Math.max(rob1 + n, rob2);
        rob1 = rob2;
        rob2 = newRob;
    }
    return rob2;
}