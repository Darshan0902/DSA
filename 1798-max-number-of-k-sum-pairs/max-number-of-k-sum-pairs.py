class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        l= 0
        nums.sort()
        n = len(nums)
        r=n-1
        operations=0
        while l < r:
            s=nums[l] + nums[r]
            if s == k:
                l+=1
                r-=1
                operations+=1
            elif s < k:
                l+=1
            else:
                r-=1
        return operations