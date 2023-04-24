/**
 * @param {number[]} temperatures
 * @return {number[]}
 */
var dailyTemperatures = function(temperatures) {
    const res = new Array(temperatures.length).fill(0);
    const stack = [];

    temperatures.forEach((t, curIdx) => {
        while (temperatures[stack?.[stack.length-1]] < t) {
            prevIdx = stack.pop();
            res[prevIdx] = curIdx - prevIdx;
        }
        stack.push(curIdx);
    });
    return res;
};