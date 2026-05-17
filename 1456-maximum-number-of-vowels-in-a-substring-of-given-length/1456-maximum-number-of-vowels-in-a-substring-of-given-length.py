class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        curcount = 0
        n  =len(s)
        for i in range(0,k):
            if s[i] in vowels:
                curcount+=1
        maxc = curcount
        for i in range(k,n):
            if s[i-k]  in vowels:
                curcount-=1
            if s[i] in vowels:
                curcount+=1
            maxc = max(curcount,maxc)
        return maxc

