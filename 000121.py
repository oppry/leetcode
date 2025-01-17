class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #prices = [10,9,3,8,10,2,6]
        #prices = [7,1,5,3,6,4]
        gain = 0
        buy = prices[0]
        for i in prices:
            if(i < buy):
                buy = i
            else:
                c = i - buy
                if(c > gain):
                    gain = c
            #print("1 - ", buy, i, gain, c)
        return gain
    