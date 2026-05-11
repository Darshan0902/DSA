class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            r = str(num)
            for ch in r:
                r1 = int(ch)
                ans.append(r1)
        return ans
