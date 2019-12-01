import sys
sys.setrecursionlimit(10000)
s = '4 5 7 3 9 6 2'
s = [int(i) for i in s.split(' ')]
k = 15
temp = []
out = []

def subset(index, sum):
    if sum == 0:
        out.append(temp.copy())
        return
    for i in range(index):
        if sum > Sum[index - i - 1]:
            break
        if sum - s[index - i - 1] >= 0:
            temp.append(s[index - i - 1])
            subset(index - i - 1,sum - s[index - i - 1])
            temp.pop()

if __name__ == '__main__':
    Sum = []
    Sum.append(0)
    for index,i in enumerate(s):
        Sum.append(Sum[index] + i)
    del Sum[0]
    print(Sum)
    subset(7,15)
    print(out)