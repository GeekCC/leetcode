import sys
import copy
sys.setrecursionlimit(10000)

S = [6,8,7,7,4,4,6,3,1,2]
# S.sort()
m = 3
out = []
outcome = []
temp = []
flag = [False]*len(S)
avr = sum(S)/m
Cnt = 0

def findset(m, sum, temp, index):
    global Cnt
    global out
    global outcome
    Cnt+=1
    subtemp = temp.copy()   #每一次从上一层迭代取temp数组作为本次迭代的初始量
    if len(outcome) != 0:  #如果已经有满足条件的结果，则跳出本次迭代， 由于outcome是全局变量，修改一次后，所有其它子情况也终止于此
        return
    if sum == 0:
        m -= 1
        out.append(subtemp)
        subtemp = []
        if m != 0:
            findset(m, avr,subtemp, 0)
            out.pop()
        else:
            outcome = copy.deepcopy(out) #多层变量时，使用深拷贝
            return
    else:
        for i in range(index, len(S)):
            if flag[i] == True:
                continue
            flag[i] = True
            if sum - S[i] >= 0:
                subtemp.append(S[i])
                findset(m, sum - S[i], subtemp, index + 1)
                if len(subtemp)!=0:
                    subtemp.pop()
            flag[i] = False

if __name__ == "__main__":
    findset(m, avr, temp, 0)
    print(outcome)
    print(Cnt)
