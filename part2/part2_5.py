import sys

data = [7,5,3,4,6,2,1]
#---------------元素从小到大排列-----------------
#依次将目标栈中元素弹出，当辅助栈顶数大于当前弹出数，压入该弹出数
#若小于，则把辅助栈中比这个弹出元素小的元素都再弹回目标栈，
#保证辅助栈的栈底是当前已知最大数，
#
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



