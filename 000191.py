def check(n):
    s = bin(n)
    count = 0
    for i in s:
        if i == "1":
            count += 1
    return count    

def check0(n):
    count = 0
    for i in range(32):
        if n & 1 << i != 0:
            count += 1
    return count

def check1(n):
    count = 0
    for i in range(32):
        if n & 1:
            count += 1
        n = n >> 1
    return count

class Solution:
    def hammingWeight(self, n: int) -> int:
        count= 0
        while n:
            n = n & (n-1)
            count += 1
        return count


