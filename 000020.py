my_dict = {
    "(":")",
    "[":"]",
    "{":"}"
}

class Solution:
    def isValid(self, s: str) -> bool:
        sta = []
        if(len(s) % 2):
            return False
        for s1 in s:
            #print(s1)
            if(s1 == "(" or s1 == "[" or s1 == "{"):
                sta.append(my_dict[s1])
            else:
                if(len(sta) == 0):
                    return False
                last = sta.pop(-1)
                #print(last, s1)
                if(s1 != last or last == None):
                    return False
        if(len(sta) != 0):
            return False
        return True

