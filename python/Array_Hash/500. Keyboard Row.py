'''
own
Time: O(w * c)  -- w: # of words; c: length of word
Space: O(w)
'''

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1, row2, row3 = "qwertyuiop", "asdfghjkl", "zxcvbnm"
        cnt = ""
        res = []

        for w in words:
            for c in w:
                if c.lower() in row1:
                    cnt += "1"
                elif c.lower() in row2:
                    cnt += "2"
                else:
                    cnt +="3" 
            if len(set(cnt)) == 1:
                res.append(w)
            cnt = ""

        return res