'''
hash
Time: O(n)
Space: O(n)
'''

class Solution:
    # own
    def maxNumberOfBalloons(self, text: str) -> int:
        hash = {
            'b': 0,
            'a': 0,
            'l': 0,
            'o': 0,
            'n': 0
        }

        for c in text:
            if c in hash:
                if c == 'b' or c == 'a' or c == 'n':
                        hash[c] += 2
                elif c == 'l' or c =='o':
                        hash[c] += 1


        return min(hash.values()) // 2
    
    def maxNumberOfBalloons(self, text: str) -> int:
        countText = Counter(text)
        balloon = Counter("balloon")

        res = float("inf")
        for c in balloon:
              res = min(res, countText[c] // balloon[c]) 

        return res
    
    def maxNumberOfBalloons(self, text: str) -> int:
         return min(text.count('b'), text.count('a'), text.count('l') // 2, text.count('o') // 2, text.count('n'))
