class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = 0
        curr_window = 0
        curr_count =0
        n = len(nums)
        max_length = 0
        for r in range(0,n):
            if nums[r] == 0:
                curr_count+=1
            while curr_count>1:
                if nums[l]==0 and curr_count>1:
                    curr_count-=1
                l+=1
            max_length = max(max_length,r-l)    
        return max_length
        