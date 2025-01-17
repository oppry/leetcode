class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        count = rowIndex + 1
        p_list = [1] * count
        n_list = [1] * count
        for i in range(1, count):
            for j in range(1, i):
                n_list[j] = p_list[j - 1] + p_list[j]
            p_list, n_list = n_list, p_list
            #print(p_list, n_list)
        return p_list
    