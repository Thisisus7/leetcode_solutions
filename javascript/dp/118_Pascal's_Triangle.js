/**
 * @param {number} numRows
 * @return {number[][]}
 */
var generate = function(numRows) {
    const res = [[1]]; 

    for (let i=0; i<numRows-1; i++) {
        const temp = [0].concat(res[res.length-1], [0]);  // [0,,] + res[res.length-1] + [,0]
        let row = [];

        for (let j=0; j<res[res.length-1].length+1; j++) row.push(temp[j] + temp[j+1]);

        res.push(row);
    }
    return res;
};