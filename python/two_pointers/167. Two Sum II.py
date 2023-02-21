'''
Two pointer:
Time: O(n)
Space: O(c)
'''

class Solution:
    # two sum I
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        map = {}

        for i in range(len(numbers)):
            complement = target - numbers[i]
            if complement in map.keys():
                return [map.get(complement)+1, i+1]
            map[numbers[i]] = i

    # two sum II
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l, r]
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                r += 1




