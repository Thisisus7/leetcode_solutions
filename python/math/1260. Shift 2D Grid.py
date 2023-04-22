'''
2D -> 1D -> 2D
Time: O(m * n)
Space: O(m * n)
'''
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        M, N = len(grid), len(grid[0])

        def TwoD2OneD(row, col):
            return row * N + col
        def OneD2TwoD(idx):
            return idx // N, idx % N

        res = [[0] * N for i in range(M)]  # new m*n grid
        
        for r in range(M):
            for c in range(N):
                newIdx1D = (TwoD2OneD(r, c) + k) % (M * N)  # %(M*N): edge case
                newR, newC = OneD2TwoD(newIdx1D)
                res[newR][newC] = grid[r][c]

        return res