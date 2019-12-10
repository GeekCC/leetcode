n = 10
data = [i+1 for i in range(n)]
temp = []
flag = [False]*n
out = []
cnt = 0

#同1_7
def search(temp, odd, flag, lastnum):
    global cnt
    global out
    cnt+=1
    if len(temp) == n:
        out.append(temp.copy())
        return
    if odd == 0:
        for i in range(int(len(data)/2)):
            if flag[i*2] == True:
                continue
            if len(temp) == n-1 and isPrime(data[2*i] + temp[0]) == False:
                return
            flag[i*2] = True
            if isPrime(data[i*2] + lastnum):
                temp.append(data[i*2])
                search(temp.copy(), 1, flag.copy(), data[i*2])
                temp.pop()
            flag[i*2] = False
    else:
        for i in range(int(len(data)/2)):
            if flag[i*2+1] == True:
                continue
            if len(temp) == n-1 and isPrime(data[i*2+1] + temp[0]) == False:
                return
            flag[i*2+1] = True
            if isPrime(data[i*2+1] + lastnum):
                temp.append(data[i*2+1])
                search(temp.copy(), 0, flag.copy(), data[i*2+1])
                temp.pop()
            flag[i*2+1] = False

def isPrime(num):
    if num < 1:
        return False
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True

if __name__ == "__main__":
    if n%2 == 1:
        print("flase")
    else:
        search(temp, 0, flag, 0)
        search(temp, 1, flag, 0)
    print(cnt)
    for i in out:
        print(i)