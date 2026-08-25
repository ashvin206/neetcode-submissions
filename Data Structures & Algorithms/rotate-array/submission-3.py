"""
Given an integer array, nums, rotate array to right by k steps where k is non-negative.

nums = [1 2 3 4 5 6 7 8]
k = 4 
nums = [5, 6, 7, 8, 1, 2, 3, 4]

Array is NOT sorted here! 

One solution could be to make a linked list out of the given array, then set the head to be whatever kth value is and return that (and something to prevent a loop from happening) 
This would require looping through nums once O(n), then going through that linked list itself O(n) and would have a time complexity of O(n). So this is one possible way of going about it. But maybe an easier way is simply dividing the list. 

So if we have [1, 2, 3, 4, 5, 6, 7, 8], and we want to rotate it 4 times, one thing to also keep in mind is that if we rotate it n times (n being length of list) then we end up in same position, so we can use some modulo logic for that. But anyways, rotate it 4 times means we want to start from 5
So we just take 5 to end, and start to 5. That feels fairly straightforward.. 

Hold on I think I'm missign something in this logic because if we rotate it once, we should expect:
[8, 1, 2, 3, 4, 5, 6, 7] 
But following this logic I'm talking about, we start at 1, but 1 isn't the actual start of our new list. That only occured in the last one because it went past the bounds of the array. 

So we have to check if k is less than or equal to hafl, or greater than half of n? 

E.g. [1, 2, 3, 4, 5, 6] 
k = 4 
Res = [3, 4, 5, 6, 1, 2] 
[3, 4, 5, 6] [1,2] 
We know that our left list should be [3, 4, 5, 6] and our right list should be [1,2] because after 4 rotations, the first number shifts to the 4th index. This means we take our right list as [0:len(nums) - k], and our left list as [len(nums) - k:]

What if k = 2 
[1, 2, 3, 4, 5, 6] 
[5, 6, 1, 2, 3, 4]
left = [5, 6] right = [1, 2, 3, 4] 
2 rotations, first number shift sto 2nd index. Right list is [0:len(nums) - k] and left list as [len(nums) - k:]

What if k = 3 
res = [4, 5, 6, 1, 2, 3] 
[4, 5, 6][1,2,3]
3 rotations, first number shifts to third index, right list is [0:len(nums) - k] and left list as [len(nums) -k:]

But I think there is a limitation in this logic that I'm missing..
"""
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums) 
        nums[:] = nums[len(nums)-k:] + nums[0:len(nums)-k]
