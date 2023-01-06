'''
Time: O(n^2) -- n: num of rows
Space: O(n^2)
'''
# temp = [0] + res[-1] + [0] is the key idea
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]  # base case: row 0

        for i in range(numRows - 1):  # already have 1 row
            temp = [0] + res[-1] + [0]  # last row, e.g., [0, 1, 0]
            row = []
            for j in range(len(res[-1]) + 1):
                row.append(temp[j] + temp[j+1])
                
            res.append(row)


        return res