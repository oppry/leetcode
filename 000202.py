def calc0(n):
    s = str(n)
    ret = 0
    for i in s:
        ret = ret + (ord(i) - ord("0")) ** 2
    return ret

def calc1(n):
    ret = 0
    while n:
        ret = ret + (n % 10) ** 2
        n = n // 10
    return ret

def check(n):
    new_n = n
    count = 1
    while new_n != 1:
        new_n = calc0(new_n)
        if(new_n == n):
            return False
        count += 1
        if count % 10 == 0:
            n = new_n
    else:
        return True

class Solution:
    def isHappy(self, n: int) -> bool:
        new_n = n
        while new_n != 1:
            new_n = calc1(new_n)
            if new_n == 4 :
                return False
        return True
