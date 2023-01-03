'''
Time: O(26*m*n) = O(m*n)  -- m: len(strs); n: avg(len(each word))
'''
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # {}: throws a KeyError if you try to get an item with a key that is not currently in the dict. 
        # defaultdict: if you try to append to a nonexistent key, it will first create the key with the default value (an empty list)
        res = defaultdict(list)  # hashmap

        for s in strs:
            count = [0] * 26  # 26 letters in total

            for c in s:
                count[ord(c) - ord('a')] += 1  # idx: [0-25] 

            res[tuple(count)].append(s)  # in python, list can't be index, so use tuple

        return list(res.values())
