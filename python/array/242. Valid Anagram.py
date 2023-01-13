'''
hashmap (own)
Time: O(n))
Space: O(n)
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash = {}

        for w in s:
            hash[w] = 1 + hash.get(w, 0)

        for w in t:
            if w not in hash or hash[w] -1 < 0:
                return False 
            hash[w] -= 1

            if hash[w] == 0:
                hash.pop(w)  # del hash[w]

        return True if len(hash) == 0 else False

    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t) 