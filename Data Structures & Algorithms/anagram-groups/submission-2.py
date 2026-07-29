"""
Go through each word, create letter dictionary
act = a:1, c:1, t:1 
Do this for each word
Instead of dictionary it should be a list of 26 0s, update based on lex
use that as key for a dictionary, value being list of the words
Go through that dictionary as they are groupedn ow 
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = dict() 
        for word in strs:
            letters = [0] * 26 
            for letter in word:
                letters[ord(letter) - 97] += 1 
            letters = tuple(letters) 
            if letters in groups:
                groups[letters].append(word)
            else:
                groups[letters] = [word]
        return list(groups.values())
