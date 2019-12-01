import sys
x = [1,[2,3],4,[5,[6,7],8],9]
print(x)
def reverse(x):
    if len(x) == 1:
        return
    else:
        for i in range(int(len(x)/2)):
            temp = x[i]
            x[i] = x[len(x)-i-1]
            x[len(x)-i-1] = temp
            if not isinstance(x[i],int):
                reverse(x[i])
            if not isinstance(x[len(x)-i-1],int):
                reverse(x[len(x)-i-1])
        if not isinstance(x[int(len(x)/2)],int):
                reverse(x[int(len(x)/2)])
    return
reverse(x)
print(x)

