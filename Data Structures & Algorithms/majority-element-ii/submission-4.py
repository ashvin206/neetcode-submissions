class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c1 = None
        c2 = None
        o1 = 0
        o2 = 0

        for i in range(len(nums)):
            num = nums[i] 
            if num == c1:
                o1 += 1 
            elif num == c2:
                o2 += 1 
            elif o1 == 0:
                c1 = num
                o1 = 1 
            elif o2 == 0:
                c2 = num 
                o2 = 1 
            else:
                o1 -=1 
                o2 -=1     
        print(c1, o1, c2, o2)
        res = [] 
        
        f1, f2 = 0, 0
        for i in range(len(nums)):
            num = nums[i] 
            if c1 == num:
                f1 += 1
            if c2 == num:
                f2 += 1 
        if f1 > len(nums)//3: 
            res.append(c1)
        if f2 > len(nums)//3:
            res.append(c2)
        return res
        
            