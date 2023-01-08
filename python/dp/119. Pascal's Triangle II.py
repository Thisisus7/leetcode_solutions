'''
(own)
Time: O(n^2)
Space: O(n)
nth row and mth column: C(n, m) = n! / (m! (n-m)!) = c(n, m-1) * ((n - m + 1) / m)
Time: O(n)
'''

class Solution:
    # own
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]

        for i in range(rowIndex):  # layers
            temp = [0] + res + [0]
            res.clear()
            for j in range(len(temp) - 1):  # elements for each layer
                res.append(temp[i] + temp[i+1])


        return res

    # formula
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1] * (rowIndex + 1)

        for i in range(1, len(res)):
            res[i] = int(res[i-1] * (rowIndex - i + 1) / i)

        return res
