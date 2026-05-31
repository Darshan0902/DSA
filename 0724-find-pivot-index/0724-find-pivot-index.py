class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        l_sum = 0
        total_sum =  sum(nums)
        for i in range(0,n):
            r_sum  = total_sum - l_sum - nums[i]
            if l_sum == r_sum:
                return i
            l_sum += nums[i]
        return -1
