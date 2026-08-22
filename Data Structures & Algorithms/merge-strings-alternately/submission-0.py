class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = 0 
        res = "" 
        while i < len(word1) and j < len(word2):
            c1 = word1[i]
            c2 = word2[j] 
            res += c1 
            res += c2 
            i += 1 
            j += 1 
        if i < len(word1):
            res += word1[i:]
        if j < len(word2):
            res += word2[j:]
        return res