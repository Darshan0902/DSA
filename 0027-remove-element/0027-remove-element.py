class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        count = 0
        l = 0
        for i in range(0,n):
            if nums[i] == val:
                count += 1

        while count > 0:
            if nums[l] == val:
                nums[l], nums[n-1] = nums[n-1] , nums[l]
                count-=1
                n-=1
            else:
                l+=1
        return n


