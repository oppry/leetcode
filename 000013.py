my_dict = {
    "I" :  1,
    "IV" : 4,
    "V" :  5,
    "IX":  9,
    "X" :  10,
    "XL":  40,
    "L" :  50,
    "XC":  90,
    "C" :  100,
    "CD":  400,
    "D" :  500,
    "CM":  900,
    "M" :  1000

}

my_dict1 = {
    "I" :  1,
    "V" :  5,
    "X" :  10,
    "L" :  50,
    "C" :  100,
    "D" :  500,
    "M" :  1000

}

def abc(s):
    sum = 0
    last = "bad"
    for lm in s:
        new = last + lm
        if(new in my_dict):
            sum = sum - my_dict[last] + my_dict[new]
        else:
            sum = sum + my_dict[lm]
        last = lm
    return sum

def abc1(s):
    sum = 0
    last = 1000
    for lm in s:
        cur = my_dict1[lm]
        sum = sum + cur
        if(last < cur):
            sum = sum - 2 * last
        last = cur
    return sum

class Solution:
    def romanToInt(self, s: str) -> int:
        sum = 0
        cur = 0
        while(cur < len(s) - 1):
            if(my_dict1[s[cur]] < my_dict1[s[cur + 1]]):
                sum += my_dict1[s[cur + 1]] - my_dict1[s[cur]]
#                print(my_dict1[s[cur + 1]], my_dict1[s[cur]], sum)
                cur = cur + 2
            else:
                sum += my_dict1[s[cur]]
#                print(my_dict1[s[cur]], sum)
                cur = cur + 1
        else:
            if(cur < len(s)):
                sum += my_dict1[s[-1]]
        return sum
    