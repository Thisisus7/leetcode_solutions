'''
Time: O(n * m)
Space: O(n)

e.g., m = 3, n = 21
28 21 15 10 6 3 1
7  6  5  4  3 2 1
1  1  1  1  1 1 1
res = 28
'''

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n  # bottom row is all 1

        for i in range(m - 1):  # the rest rows
            newRow = [1] * n  # initialize upper rows
            for j in range(n - 2, -1 , -1):  # except the last element in each row
                newRow[j] = row[j] + newRow[j + 1]  # bottom + right
            row = newRow

        return row[0]  # the 1st value is the start point 