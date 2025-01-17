def generate_next(p_list):
    n_list = [1]
    for i in range(1, len(p_list)):
        n_list.append(p_list[i - 1]+p_list[i])
    n_list.append(1)
    return n_list



class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ret_list = [[1]]
        c_list = [1]
        for i in range(1, numRows):
            c_list = generate_next(c_list)
            ret_list.append(c_list)
        return ret_list
