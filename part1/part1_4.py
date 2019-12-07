str1='adacbcb'
str2='abdebcbb'
num = [[0]*len(str2) for i in range(len(str1))] #一个演示数组
maxlen = 0
maxsub = []

def LCS(str1, str2, index1, index2, strlen, substr):
    global maxlen
    global maxsub
    sub = substr.copy()
    if index1 == len(str1) or index2 == len(str2):
        return
    if str1[index1] == str2[index2]:
        sub.append(str1[index1])
        strlen += 1
        if strlen > maxlen:
            maxlen = strlen
            maxsub = sub
        num[index1][index2] = 1
        LCS(str1, str2, index1+1, index2+1, strlen, sub)
    else:
        LCS(str1, str2, index1+1, index2, strlen, sub)
        LCS(str1, str2, index1, index2+1, strlen, sub)

LCS(str1, str2, 0, 0, 0, substr = [])
print("   ",end='')
for i in str2:
    print(i,' ',end='')
print()
for i in range(len(str1)):
    print(str1[i], num[i][:])

print("MaxSubStr:",maxsub)


