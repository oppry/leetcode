class Solution:
    def reverseBits(self, n: int) -> int:
        s = bin(n)[:1:-1]
        #print(s)
        s = s + "0" * (32 - len(s))
        return int(s, 2)
    