class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = 0
        n = len(nums)
        curr = 0
        maxc = 0
        for i in range(0,n):
            if nums[i] == 0:
                curr+=1
            while curr > 1:
                if nums[l] == 0 and curr > 1:
                    curr-=1
                l+=1
            maxc = max(i-l , maxc)
        return maxc

