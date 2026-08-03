class Solution:
    def getLetters(self, strs, i): 
        mySet = set()
        for word in strs:
            if word:
                mySet.add(word[i])
            else:
                mySet.add("")
        return mySet
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = "" 
        smallestWordIndex = 0 
        for i in range(len(strs)):
            if len(strs[i]) < len(strs[smallestWordIndex]):
                smallestWordIndex = i 
        for i in range(len(strs[smallestWordIndex])):
            s = self.getLetters(strs, i)
            if len(s) == 1:
                prefix += s.pop() 
            else:
                break
        return prefix