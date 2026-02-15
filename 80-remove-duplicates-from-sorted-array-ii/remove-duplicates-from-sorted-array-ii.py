class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 1
        l = 1
        n= len(nums)
        for r in range(1,n):
            if nums[r] == nums[r-1]:
                count+=1
            else:
                count=1
            if count <=2:
                nums[l] = nums[r]
                l+=1
        return l