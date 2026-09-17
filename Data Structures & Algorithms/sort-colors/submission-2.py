class Solution:
    def sortColors(self, nums: List[int]) -> None:
        ls = [0, 0, 0] 
        for num in nums:
            if num == 0:
                ls[0]+=1 
            elif num == 1:
                ls[1]+=1 
            elif num == 2:
                ls[2]+=1
        i = 0 
        j = 0 
        for num in ls:
            while num > 0:
                nums[i] = j
                i += 1 
                num -= 1 
            j += 1 
            