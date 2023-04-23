'''
Time: O(nlogn)  -- sorting
'''

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i : i[0])  # sort by 1st value of each interval
        output = [intervals[0]]  # initialize with the 1st interval

        for start, end in intervals[1:]:  # current start/ends
            lastEnd = output[-1][1]

            if start <= lastEnd:  # overlapping
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])

        return output