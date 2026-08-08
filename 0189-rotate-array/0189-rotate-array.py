class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        while k > 0:
            el = nums.pop()
            nums.insert(0,el)
            k-=1
        return nums