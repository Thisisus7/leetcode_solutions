/**
 * @param {number[][]} mat
 * @param {number} r
 * @param {number} c
 * @return {number[][]}
 */
var matrixReshape = function(mat, r, c) {
    if (mat.length * mat[0].length != r * c) return mat;

    const flat_mat = mat.flat();
    const res = [];
    
    for (let i=0; i<r; i++) {
        const row = [];
        for (let j=0; j<c; j++) row.push(flat_mat[c*i + j]);

        res.push(row);
    }
    return res;
};