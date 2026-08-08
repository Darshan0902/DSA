from math import gcd

class Solution:
    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:
        n = len(arr)
        g = gcd(n, k)

        ans = 0

        for start in range(g):
            group = []

            for i in range(start, n, g):
                group.append(arr[i])

            group.sort()
            median = group[len(group) // 2]

            for num in group:
                ans += abs(num - median)

        return ans