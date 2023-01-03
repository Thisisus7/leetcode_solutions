'''
set(): O(1) lookup/insert/delete
Time: O(n)
Space: O(n)
'''

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in numSet:
            if n-1 not in numSet:  # if n is the first number of a sequence
                length = 0

                while n+length in numSet:  # first number: n + 0 == n
                    length += 1
                
            longest = max(longest, length)

        return longest