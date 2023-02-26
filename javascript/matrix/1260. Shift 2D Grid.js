/**
 * @param {number[][]} grid
 * @param {number} k
 * @return {number[][]}
 */
var shiftGrid = function(grid, k) {
    const M = grid.length, N = grid[0].length;

    const posToIdx = (row, col) => {
        return row * N + col;
    }
    const idxToPos = (idx) => {
        return [Math.floor(idx / N), idx % N];  // can only return 1 value
    }

    let res = Array(M).fill().map(() => Array(N));
    for (let r=0; r<M; r++) {
        for (let c=0; c<N; c++) {
            let newIdx = (posToIdx(r, c) + k) % (M * N);
            let [newR, newC] = idxToPos(newIdx);
            res[newR][newC] = grid[r][c];
        }
    }
    return res;
};