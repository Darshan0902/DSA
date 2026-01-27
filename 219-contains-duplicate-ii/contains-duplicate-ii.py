class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        unique = set()
        l = 0
        n = len(nums)
        for r in range(0,n):
            if nums[r] in unique:
                return True
            
            unique.add(nums[r])

            if r - l == k:
                unique.remove(nums[l])
                l+=1
        return False