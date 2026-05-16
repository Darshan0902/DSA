class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n =len(nums)
        window_sum =sum(nums[:k])
        l = 0
        maxed = window_sum
        for r in range(k,n):
            window_sum += nums[r]
            window_sum -=  nums[l]
            l+=1
            maxed = max(window_sum ,maxed)
        return maxed/k