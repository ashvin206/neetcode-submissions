class Solution:
    def sortColors(self, nums: List[int]) -> None:
        ls = [0, 0, 0] 
        for num in nums:
            ls[num] += 1 
        j = 0 
        for i in range(3):
            while ls[i]:
                ls[i] -= 1 
                nums[j] = i 
                j += 1 
        