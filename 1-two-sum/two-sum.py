class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index , value in enumerate(nums):
            remaining = target - value
            if remaining in seen:
                return(seen[remaining],index)
            else:
                seen[value] = index
