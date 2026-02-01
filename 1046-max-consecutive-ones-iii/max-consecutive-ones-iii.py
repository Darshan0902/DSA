class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l  = 0
        curr = 0
        n =  len(nums)
        max_length = 0
        for r in range(0,n):
            if nums[r] == 0:
                curr+=1
            while k<curr:
                if  nums[l]==0:
                    curr-=1
                l+=1
            max_length = max(max_length,r-l+1)
        return max_length
            
                