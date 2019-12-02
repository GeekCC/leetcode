import sys

data = [7,5,3,4,6,2,1]

def stack_sort(s):
    stack = s
    temp = []
    while len(stack) != 0:
        max = stack[len(stack)-1]
        stack.pop()
        while len(temp) != 0 and max > temp[len(temp)-1]:
            stack.append(temp.pop())
        temp.append(max)
    while len(temp) != 0:
        stack.append(temp.pop())
    return stack
if __name__ == "__main__":
    print(stack_sort(data))



