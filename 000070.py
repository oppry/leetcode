class Solution:
    def climbStairs(self, n: int) -> int:
        if(n == 1):
            return 1
        ff0 = 1
        ff1 = 1
        for i in range(2, n + 1):
            a = ff1
            ff1 = ff1 + ff0
            ff0 = a
        return ff1
