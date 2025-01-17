def code_s0(s):
    d = {}
    sign = 0
    for i in s:
        if i not in d:
            d[i] = sign
            sign += 1
    l = []
    for i in s:
        l.append(d[i])
    return l

def code_s(s):
    d = {}
    l = []
    sign = 0
    for i in s:
        if i not in d:
            d[i] = sign
            sign += 1
        l.append(d[i])
    return l

def code_s_error(s):
    d = {}
    ret = 0
    sign = 0
    for i in s:
        if i not in d:
            d[i] = sign
            sign += 1
        ret = ret + d[i]
    return ret

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        #print(code_s(s), code_s(t))
        #return code_s(s) == code_s(t)
        return True if [s.index(i) for i in s] == [t.index(j) for j in t] else False
    