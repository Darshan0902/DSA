class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []

        for n in nums:
            t = 0
            temp = n
            while temp & 1:
                t += 1
                temp >>= 1

            if t == 0:
                ans.append(-1)
            else:
                ans.append(n - (1 << (t - 1)))

        return ans