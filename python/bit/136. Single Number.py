'''
(own): wrong
Time: O(n)
Space: O(n)
exclusive or (XOR): 1^0 = 1; 0^0 = 0, 1^1 = 0
Time:O(n)
Space: O(1)
'''

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        record = set()

        for n in nums:
            if n not in record:
                record.add(n)
            else:
                record.remove(n)

        return record.pop()  # list(record)[0]; next(iter(record)); min(record)

    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            res ^= n

        return res

    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x ^ y, nums)
