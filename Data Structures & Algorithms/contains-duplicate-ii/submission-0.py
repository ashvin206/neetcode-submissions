"""
nums, k 
Return true if there are two indices such taht nums[i] == nums[j] and abs(i -j) <=k
So basically, two distinct indices where we have the same number, and their absolute difference is less than or equal to some value k. 

nums = [1, 2, 3, 1] 
k = 3 
Here, 1 occurs twice, so logically nums[i] == nums[j] such that i = 0, j = 3 
And since j - i is 3, 3 <= 3 so this is true 

What if we track a dictionary with num:index as the key:value pairs 
[1:[0, 3], 2:[1], 3:[2]]
Then, we go through each number in the dictionary where len(value) > 1: and logically it should be sorted, so we can just start iwht testing the two smallest values first, then the next two, so like a sliding window. 
"""
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        numIndex = dict()
        for i in range(len(nums)):
            if nums[i] in numIndex:
                numIndex[nums[i]].append(i)
            else:
                numIndex[nums[i]] = [i]
        for ls in numIndex.values():
            print(ls)
            if len(ls) > 1:
                # sliding window logic 
                l = 0 
                r = 1 
                while r < len(ls):
                    if abs(ls[r] - ls[l]) <= k: 
                        return True
                    l += 1
                    r += 1 
        return False

