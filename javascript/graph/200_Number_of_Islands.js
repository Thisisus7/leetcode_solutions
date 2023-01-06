/**
 * @param {character[][]} grid
 * @return {number}
 */
// Solution 1
var numIslands = function(grid) {
    if (!grid) return 0;

    const visited = new Set();
    const rows = grid.length, cols = grid[0].length;
    let islands = 0;
  
    function bfs(r, c) {
      const q = [];
      visited.add(`${r},${c}`);  // can't use [r, c] and (r, c)
      q.push([r, c]);
  
      while (q.length) {
        const [row, col] = q.shift();
        const directions = [[-1, 0], [1, 0], [0, -1], [0, 1]];
  
        for (let [dr, dc] of directions) {
          const r = row + dr, c = col + dc;
          // can't use 0 <= r < rows
          if ((0 <= r && r < rows) && (0 <= c && c < cols) && (grid[r][c] == "1") && (!(visited.has(`${r},${c}`)))) {
            visited.add(`${r},${c}`);
            q.push([r, c]);
          }
        }
      }
    }
  
    for (let r = 0; r < rows; r++) {
      for (let c = 0; c < cols; c++) {
        if ((grid[r][c] == "1") && (!(visited.has(`${r},${c}`)))) {
          bfs(r, c);
          islands++;
        }
      }
    }
    return islands;
};

// solution 2
var numIslands = function(grid) {
    if (!grid) return 0;
  
    const rows = grid.length, cols = grid[0].length;
    let islands = 0;
  
    function dfs(r, c) {
      if ((0 <= r && r < rows) && (0 <= c && c < cols) && (grid[r][c] == "1")) {
        grid[r][c] = "0";
        dfs(r - 1, c);
        dfs(r + 1, c);
        dfs(r, c - 1);
        dfs(r, c + 1);
      }
    }
  
    for (let r = 0; r < rows; r++) {
      for (let c = 0; c < cols; c++) {
        if (grid[r][c] == "1") {
          dfs(r, c);
          islands++;
        }
      }
    }
    return islands;
  };