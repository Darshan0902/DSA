class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l = 0
        curr_count=sum(nums[:k])
        max_sum = curr_count  
        for i in range(k,len(nums)):
            curr_count -= nums[i-k]
            curr_count+= nums[i]
            max_sum  = max(curr_count,max_sum)  
        return max_sum /  k