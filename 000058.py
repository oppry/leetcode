class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        cur = 0
        for i in reversed(s):
            if(cur == 0 and i == " "):
                continue
            if i == " ":
                return cur
            cur += 1
        return cur
