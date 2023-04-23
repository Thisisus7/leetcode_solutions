'''
Two hash (own)
Time: O(len(s))
Space: O(len(pattern))
How to be more elegant: convert str to list
Two hash
Time: O(m + n)
Space: O(m + n)
'''
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # edge case: if pattern and s have same number of elements
        s += " "
        if s.count(" ") != len(pattern):
            return False

        # main
        hashPS, hashSP = {}, {}
        cnt = 0
        word = ""
        for c in s:
            if not c.islower():  # .split()
                if (((pattern[cnt] in hashPS) and (hashPS[pattern[cnt]] != word)) or 
                    ((word in hashSP) and (hashSP[word] != pattern[cnt]))):
                    return False

                hashPS[pattern[cnt]] = word
                hashSP[word] = pattern[cnt]
                word =""
                cnt += 1
            else:
                word += c

        return True
    
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(words) != len(pattern):
            return False
        
        p2str, str2p = {}, {}
        for p, w in zip(pattern, words):
            if ((p in p2str and p2str[p] != w) or 
                (w in str2p and str2p[w] != p)):
                return False
            
            p2str[p] = w
            str2p[w] = p

        return True


        


