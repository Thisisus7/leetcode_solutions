'''
Time: O(n^2)
Space: O(1)
'''

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(matrix[0])-1  # row pointers  !!! -1

        while l < r:  # layer 
            for i in range(r - l):  # element for each layer
                t, b = l ,r  # column pointers: top, bottom 

                topLeft = matrix[t][l + i]  # save the top left value
                matrix[t][l + i] = matrix[b - i][l]  # bottom left -> top left
                matrix[b - i][l] = matrix[b][r - i]  # bottom right -> bottom left
                matrix[b][r - i] = matrix[t + i][r]  # top right -> bottom right
                matrix[t + i][r] = topLeft  # top left -> top right

            l += 1
            r -= 1