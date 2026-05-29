class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = 0
        n = len(nums)
        curr =  0
        res =0
        for i in range(0,n):
            if nums[i] == 0:
                curr+=1
            while curr > 1:
                if nums[l] == 0:
                    curr-=1
                l+=1
            res = max(res,i-l) 
        return res