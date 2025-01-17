class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        cur = columnNumber
        ret = ""
        while cur > 0:
            cur = cur - 1
            re0 = cur % 26
            ret = chr(re0 + ord("A") ) + ret
            cur = (cur - re0) // 26
            #print(cur, re0, ret)
        return ret
    