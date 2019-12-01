# def LCS(strA,strB):
#     lenA = len(strA)
#     lenB = len(strB)
#     out = []    
#     N = [[0]*(lenB+1) for i in range(lenA+1)]
#     H = [[0]*(lenB+1) for i in range(lenA+1)]
#     for i in range(1,lenA+1):
#         for j in range(1,lenB+1):
#             if strA[i-1] == strB[j-1]:
#                 N[i][j] = N[i-1][j-1]+1
#                 H[i][j] = 1
#                 break
#             elif N[i][j-1] >= N[i-1][j]:
#                 N[i][j] = N[i][j-1]
#                 H[i][j] = 'n'
#             else:
#                 N[i][j] = N[i-1][j]
#                 H[i][j] = 'top'
#     print(N)
#     print(H)
#     return out

# def main():
#     strA = input()
#     strB = input()
#     print(LCS(strA,strB))

# if __name__=='__main__':
#     main()
cnt = 0
str1='adacbcb'
str2='abdebcbb'
num = [[0]*len(str2) for i in range(len(str1))]
def LCS(str1, str2, index1, index2):
    global cnt
    if index1 == len(str1) or index2 == len(str2):
        return
    if str1[index1] == str2[index2]:
        num[index1][index2] = 1
        LCS(str1, str2, index1+1, index2+1)
    else:
        LCS(str1, str2, index1+1, index2)
        LCS(str1, str2, index1, index2+1)

# str1 = input()
# str2 = input()
# def Search(matrix, row, col):
#     while(col < len(str2)):
#         if matrix[row][col] == 1:
#             Search(matrix, row+1， col+1)
#         col += 1

LCS(str1, str2, 0, 0)
print("   ",end='')
for i in str2:
    print(i,' ',end='')
print('\n')
for i in range(len(str1)):
    print(str1[i], num[i][:])




