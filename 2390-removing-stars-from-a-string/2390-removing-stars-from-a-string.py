class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        star = "*"
        for ch in s:
            if ch == star:
                stack.pop()
            else:
                stack.append(ch)
        return "".join(stack)