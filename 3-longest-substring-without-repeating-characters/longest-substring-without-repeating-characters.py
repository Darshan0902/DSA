class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        l =0
        r =n-1
        res=0
        unique=set()
        for r in range(0,n):
            while s[r] in unique:
                unique.remove(s[l])
                l+=1
            unique.add(s[r])
            res=max(res,r-l+1)
        return res
            





        