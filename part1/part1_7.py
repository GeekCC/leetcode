import sys

S = [6,8,7,7,4,4,6,3,1,2]
S.sort()
m = 3
out = []
temp = []
flag = [False]*len(S)
avr = sum(S)/m

def findset(flag, m, sum, index):
    global out
    if m == 1:
        return
    if sum == 0:
        m -= 1
        out.append(temp.copy())
        findset(flag, m - 1, avr, 0)
        print(temp)
        out.pop()

    for i in range(index, len(S)):
        if flag[i] == True:
            continue
        flag[i] = True
        if sum - S[i] >= 0:
            temp.append(S[i])
            findset(flag, m, sum - S[i], index + 1)
            temp.pop()
        flag[i] = False


if __name__ == "__main__":
    findset(flag, m, avr, 0)
    print(out)

