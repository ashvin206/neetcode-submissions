class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        frequency = dict()
        for i in range(len(nums)):
            frequency[nums[i]] = frequency.get(nums[i], 0) + 1 
            if frequency[nums[i]] > len(nums)//2:
                return nums[i]
            
