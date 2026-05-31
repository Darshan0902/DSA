class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n = len(gain)
        max_alt = 0
        curr = 0
        for i in range(0,n):
            curr = sum(gain[:i+1])
            max_alt  = max(curr ,max_alt)
        return max_alt