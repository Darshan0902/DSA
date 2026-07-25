class Solution:
    def maxProduct(self, n: int) -> int:
        digits = [int(d) for d in str(n)]

        ans = 0
        m = len(digits)

        for i in range(m):
            for j in range(i + 1, m):
                ans = max(ans, digits[i] * digits[j])

        return ans