/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */
var merge = function(intervals) {
    intervals.sort((a, b) => a[0] - b[0]);
    let output = [intervals[0]];

    for (let [start, end] of intervals.slice(1)) {
        const lastEnd = output[output.length-1][1];
        if (start <= lastEnd) output[output.length-1][1] = Math.max(lastEnd, end);
        else output.push([start, end]);
    }
    return output;
};