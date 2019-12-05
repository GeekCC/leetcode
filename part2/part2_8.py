import sys

data = [[0,-2,-7,0],
        [9,2,-6,2],
        [-4,1,-4,1],
        [-1,8,0,-2]]

# 思想同2_7  动态规划状态转移  时间复杂度 o(n^3) 
def max_matrix(matrix):
    max_submatrix_sum = matrix[0][0]
    max_submatrix_start_row = 0
    max_submatrix_start_col = 0
    max_submatrix_end_col = 0
    max_submatrix_end_row = 0

    for matrix_col_len in range(1,len(matrix[0])+1):
        for start_col in range(len(matrix[0])+1 - matrix_col_len):
            maxseq = sum(matrix[0][start_col:start_col + matrix_col_len])
            end_index  = 0
            trans = [0] * len(matrix[0])
            trans[0] = sum(matrix[0][start_col:start_col + matrix_col_len])
            for i in range(1, len(matrix[0])):
                if sum(matrix[i][start_col:start_col + matrix_col_len]) > sum(matrix[i][start_col:start_col + matrix_col_len]) + trans[i-1]:
                    trans[i] = sum(matrix[i][start_col:start_col + matrix_col_len])
                else:
                    trans[i] = sum(matrix[i][start_col:start_col + matrix_col_len]) + trans[i-1]
                    if trans[i] >= maxseq:
                        maxseq = trans[i]
                        end_index = i
            
            if maxseq <= 0:
               start_row_index = end_index 
            else:
                start_row_index = end_index
                while trans[start_row_index] > 0 and start_row_index >= 0:
                    start_row_index -= 1
                start_row_index += 1
            if maxseq > max_submatrix_sum:
                max_submatrix_sum = maxseq
                max_submatrix_start_row = start_row_index
                max_submatrix_start_col = start_col
                max_submatrix_end_col = start_col + matrix_col_len - 1
                max_submatrix_end_row = end_index
    out = []
    for i in range(max_submatrix_start_row, max_submatrix_end_row+1):
        out.append(matrix[i][max_submatrix_start_col:max_submatrix_end_col+1])

    return max_submatrix_sum, out



if __name__ == "__main__":
    print(max_matrix(data))