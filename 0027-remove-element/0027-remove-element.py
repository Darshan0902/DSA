class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        l= 0
        count = 0
        for i in range(0,n):
            if nums[i] == val:
                count+=1
        
        while count > 0:
            if nums[l]==val:
                nums[n-1],nums[l] = nums[l],nums[n-1]
                n-=1
                count-=1
            else:
                l+=1
        return n 

        