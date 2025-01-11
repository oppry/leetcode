def huiwen(x):
    if(x < 0):
        return False
    a = list(str(x))
    b = a.copy()
    a.reverse()
    if(a == b):
        return True
    else:
        return False

def huiwen2(x):
        b = x
        c = 0
        a = 0
        if(x < 0):
            return False
        while(b):
            c = b % 10
            a = a * 10 + c 
            b = int((b - c) / 10)
        if(a == x):
            return True
        else:
            return False

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return huiwen(x)

