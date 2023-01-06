'''
Time: O(m*n)
'''
import collections

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:  # if no grid, islands = 0
            return 0
        
        rows, cols = len(grid), len(grid[0])  # num of rows, num of cols
        visited = set()  # islands have been visited 
        islands = 0  # num of islands

        # 1 island contain how many "1"s
        def bfs(r, c):
            q = collections.deque()
            visited.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft()  # dfs: q.pop()
                directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # left, right, above, bottom

                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(rows)) and (c in range(cols)) and (grid[r][c] == "1") and ((r, c) not in visited):
                        q.append((r, c))
                        visited.add((r, c))


        # how many islands
        for r in range(rows): 
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1

        return islands