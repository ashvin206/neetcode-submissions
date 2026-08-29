"""
abbda 

l at 0, r at 4 
a == a 
l at 1, r at 3 
b != d, since before d matches with l, delete d? 
l at 1 still, r would be at 2 now 
b == b 
done, so it passes 

aca 
l at 0, r at 2 
a == a
l at 1, r at 1, done, passes 

abbadc 
l at 0, r at 5 
a != c, 

eceec 
l = 0, r = 4 
e != c, but notice that either case works.. 
But let's say we take the left side increment, so our string is basically ceec, so thats valid 

But take the other case, ecee, this would be invalid, and this is the case taht goes first so it returns false 

Might be easier to mke isPalindrome function and call it both ways 
"""
class Solution:
    def isPalindrome(self, s, ls):
        l = 0
        r = len(s) - 1 
        while l < r:
            if s[l] != s[r]:
                ls.append(l)
                ls.append(r)
                return False 
            l += 1 
            r -= 1 
        ls.append(l)
        ls.append(r)
        return True 
    def validPalindrome(self, s: str) -> bool:
        numDel = 0 
        ls = [] 
        if not self.isPalindrome(s, ls):
            l = ls[0]
            r = ls[1]
            return self.isPalindrome(s[l:r], ls) or self.isPalindrome(s[l + 1:r + 1], ls)   
        return True 