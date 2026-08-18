"""
Hash map, key value is prefix sum, value is count of that prefix sum 
But why will this help us? 

E.g. 
[1, 1, 1, 1, 1, 1] 
k = 3 
We start at [1] , then [1, 1] then [1, 1, 1] and now our sum is 3. This means we found one subarray so far. Going to the next element, our sum is 4, and we can keep going. Next we can go to the next element and all of this is brute force with a time complexity of O(n^2).

But the thing is, we are repeating a sum that we already kept tracked of. 

sum - k gives us the number to chop off to give us a contiguous subarray, but this can apply in multiple places. 

So with that example:
[1, -1, 1, 1, 1, 1]
The options are
[1, -1, 1, 1, 1]
[-1, 1, 1, 1, 1] 
[1, 1, 1]
[1, 1, 1] 
prefix sum: [1, 0, 1, 2, 3, 4] k = 3 
1 - 3 not in hashmap, add 1 to hashmap {0:1, 1: 1} 
0 - 3 not in hashmap, add 0 to hasmap {0:2, 1:1} 
1 - 3 not in hashmpa, add 1 to hashmap {0:2,1:2} 
2 - 3 not in hashmap, add 2 to hashmap {0:2,1:2,2:1}
3-3 = 0 in hashmap, increment res by 2 and add to map {0:2, 1:2, 2:1, 3:1} 
4-3=1 in hashmap, increment res by 2 and add to map 
done! 
"""
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        frequency = {0:1} 
        prefixSum = 0 
        res = 0 
        for num in nums: 
            prefixSum += num 
            if prefixSum - k in frequency: 
                res += frequency[prefixSum - k] 
            frequency[prefixSum] = frequency.get(prefixSum, 0) + 1 
        return res
        