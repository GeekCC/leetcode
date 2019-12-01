import sys
A = [3,1,6,4,5,7,9,8,10,14,12]
stack = []
premax = A[0]

def findmid():
    global stack
    global premax
    for i in A:
        if len(stack) == 0 and i >= premax:
            stack.append(i)
            if i > premax:
                premax = i
            continue
        if len(stack) != 0:
            if i > stack[len(stack)-1]:
                stack.append(i)
                if i > premax:
                    premax = i
            else:
                if i > premax:
                    premax = i
                stack.pop()
                continue
            

if __name__ == "__main__":
    findmid()
    print(stack)
    
