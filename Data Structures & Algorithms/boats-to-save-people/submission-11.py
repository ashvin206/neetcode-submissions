"""
[1, 3, 2, 3, 2] limit = 3 
sort 
[1, 2, 2, 3, 3] 
1 + 3 = 4 
since people[r] > limit, need one boat for this, right pointer shift
l still at 1, r at 3, numBoats = 1 
same thing
l still at 1, r at 2, numBoats = 2 
1 + 2 == 3, shift boht, numBoats = 3 
l at 
"""
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort() 
        l = 0 
        r = len(people) - 1 
        numBoats = 0 
        while l <= r: 
            sumWeight = people[l] + people[r]
            if l == r:
                numBoats += 1 
                break
            elif people[l] >= limit:
                numBoats += 1 
                l += 1 
            elif people[r] >= limit:
                numBoats += 1 
                r -= 1 
            elif sumWeight <= limit:
                numBoats += 1 
                l += 1 
                r -= 1 
            elif sumWeight > limit: 
                numBoats += 1 
                r -= 1 
        return numBoats
