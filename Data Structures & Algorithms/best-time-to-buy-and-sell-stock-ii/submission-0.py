"""
1 - 7 = -6 
5 - 1 = 4 
3 - 5 = - 2
6 - 3 =3 
4 - 6 = -2 
[-6, 4, -2, 3, -2, -2] 
There is a positive price difference between day 2 and 3 
and day 4 and 6 

[1, 2, 3, 4, 5] 
[1, 1, 1, 1] 

Do we literally just sum that?? 
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            dif = prices[i] - prices[i - 1]
            if dif > 0:
                profit += dif
        return profit