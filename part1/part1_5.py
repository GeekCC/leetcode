import sys
num = input()
# num = num.split(',')
# print(num)
# for index,i in enumerate(num):
#     num[index] = int(i)
#     1
k = int(input())
def pailie(num, k):
        k -= 1
        if k >=1:
            return[i + j for i in num for j in pailie(num, k)]
        else:
            return [i for i in num]
print(pailie(num,k))