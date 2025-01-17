class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        s = reversed(columnTitle)
        loc, re = 1, 0
        for i in s:
            re = re + (ord(i) - ord("A") + 1) * loc
            loc *= 26
        return re

