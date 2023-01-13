'''
hashMap (own)
Time: O(n)
Space: O(n)
sliding window
Time: On
Space: O(k)
'''

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash = {}  # hash map

        for i in range(len(nums)):
            if nums[i] in hash and abs(i - hash[nums[i]]) <= k:
                return True
            
            hash[nums[i]] = i

        return False

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        q = set()

        for i, x in enumerate(nums):
            if i > k:
                q.remove(nums[i-k-1])  # e.g., i=3, k=2, remove(nums[3-2-1=0])

            if x in q:
                return True

            q.add(x)

        return False