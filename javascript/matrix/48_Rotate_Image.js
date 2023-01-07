/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var rotate = function(matrix) {
    let l = 0, r = matrix.length-1;

    while (l < r) {
        let t = l, b = r;
        for (let i=0; i<(r-l); i++) {
            let topLeft = matrix[t][l + i];
            matrix[t][l + i] = matrix[b - i][l]; 
            matrix[b - i][l] = matrix[b][r - i]; 
            matrix[b][r - i] = matrix[t + i][r]; 
            matrix[t + i][r] = topLeft;
        }
        l ++;
        r --;
    }
};