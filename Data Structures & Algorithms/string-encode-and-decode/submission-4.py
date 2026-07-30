"""
[Hello, World]
[5]Hello[5]World 
[0][2]vn 
Take number between [] 
Go that many characters after ] 
Combine and append to list 
"""
class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = "" 
        for word in strs: 
            length = len(word)
            encoded += "[" + str(length) + "]" + word 
        return encoded
    def decode(self, s: str) -> List[str]:
        i = 0 
        res = [] 
        while i < len(s): 
            j = i + 1
            while s[j] != "]":
                j += 1 
            length = int(s[i + 1:j])
            start = j + 1 
            end = start + length
            res.append(s[start:end])
            i = end 
        return res

