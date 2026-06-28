class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current  = ""
        repeat = 0
        for ch in s:
            if ch.isdigit():
                repeat = repeat * 10 + int(ch)
            elif ch == "[":
                stack.append(current)
                stack.append(repeat)
                current =  ""
                repeat = 0
            elif ch == "]":
                times = stack.pop()
                prev = stack.pop()
                current = prev  + current * times
            else:
                current += ch
        return current