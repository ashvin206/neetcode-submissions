class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        frequency = dict() 
        for i in range(len(nums)):
            frequency[nums[i]] = frequency.get(nums[i], 0) + 1
            # check key associated with max value, if greater than len/2, return
            key = max(frequency, key=frequency.get)
            if frequency[key] > len(nums)//2:
                return key
            
