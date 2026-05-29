class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels =set('aeiou')
        l =  0
        n  =len(s)
        curr = 0
        for i in range(k):
            if s[i] in vowels:
                curr+=1
        maxc = curr
        for i in range(k,n):
            if s[i-k] in vowels:
                curr-=1
            if s[i] in vowels:
                curr+=1
            maxc = max(maxc , curr)
        return maxc
