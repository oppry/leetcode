class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        wh = True
        cur = 0
        if(len(strs) == 0 or strs[0] == ""):
            return ""
        while(wh):
            comm = strs[0][cur]
            #print(cur, comm)
            for i in range(1, len(strs)):
                if(cur >= len(strs[i]) or strs[i][cur] != comm):
                    wh = False
                    break
            else:
                #print(cur)
                cur += 1
                if(cur >= len(strs[0])):
                    wh = False
                    break
        return strs[0][:cur]
