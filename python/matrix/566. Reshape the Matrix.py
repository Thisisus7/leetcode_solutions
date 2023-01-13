'''
(own)
Time: O(n)
Space: O(n)
'''

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        # check illegal
        if len(mat) * len(mat[0]) != r * c:
            return mat

        flat = [item for row in mat for item in row]
        res = []
        for i in range(r):
            row = []
            for j in range(c):
                row.append(flat[c*i+j])

            res.append(row)

        return res