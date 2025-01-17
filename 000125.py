class Solution:
    def isPalindrome(self, s: str) -> bool:
        #s = "0P"
        o_str = ""
        n_str = ""

        for i in s:
            if i >= "A" and i <= "Z":
                o_str += i.lower()
            if(i >= "a" and i <= "z"):
                o_str += i
            if(i >= "0" and i <= "9"):
                o_str += i
        n_str = o_str[::-1]
        #print(o_str)
        #print(n_str)

        return o_str == n_str
    