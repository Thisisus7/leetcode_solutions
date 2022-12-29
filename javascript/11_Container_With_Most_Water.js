/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    let l = 0, r = height.length - 1;
    let res = 0;

    while (l < r) {
        area = Math.min(height[l], height[r]) * (r - l);
        res = Math.max(area, res);

        if (height[l] < height[r]) l++;
        else r--;
    }
    return res;
};