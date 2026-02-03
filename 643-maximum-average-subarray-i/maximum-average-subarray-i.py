class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n  =  len(nums)
        l = 0
        window_sum = sum(nums[:k])
        max_sum=window_sum
        for r in range(k,n):
            window_sum += nums[r]
            window_sum -= nums[l]
            l+=1
            max_sum  = max(window_sum,max_sum)
        return max_sum/k