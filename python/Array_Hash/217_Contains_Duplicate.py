'''
Brute force:
Time: O(n^2)
Space: O(1)
Sorting:
Time: O(nlogn)  logn: sort
Space: O(1)
HashSet (insert: O(1)):
Time: O(n)
Space: O(n)
'''

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True

            hashset.add(n)

        return False
