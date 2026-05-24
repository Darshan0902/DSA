class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        curr = 0
        n = len(s)
        for i in range(k):
            if s[i] in vowels:
                curr+=1
        max_c = curr
        for i in range(k,n):
            if s[i-k]  in vowels:
                curr -=1
            if s[i] in vowels:
                curr+=1
            max_c = max(curr,max_c)
        return max_c

