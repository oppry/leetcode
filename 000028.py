class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        #haystack = "sadbutsad"
        #needle = "sad"
        max_loop = len(haystack) - len(needle)
        i = -1
        while(i < max_loop):
            cur = 0
            i += 1
            #print(f"begin loop {i}  ------->")
            for j in needle:
                #print(f"   compare {i + cur} - {haystack[i + cur]} : {needle.index(j)} - {j}")
                if(haystack[i + cur] != j):
                    break
                cur += 1
            else:
                return i
        else:
            return -1
