class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l=0
        n = len(nums)
        curr = 0
        res = 0
        for i in range(0,n):
            if nums[i] == 0:
                curr+=1
            while curr > k :
                if nums[l] == 0:
                    curr-=1
                l+=1
            res = max(res,i-l+1)
        return res
                
            
            
            
