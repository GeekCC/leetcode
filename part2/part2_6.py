import numpy as np

A = np.sort(np.random.randint(0,50,[8,]))
B = np.sort(np.random.randint(0,50,[8,]))
C = np.sort(np.random.randint(0,50,[8,]))

#三元组最小值由三个有序序列（升序）的当前的最小值决定， 
def search_triple(a, b ,c):
    index1 = index2 = index3 = 0
    while True:
        min = triple_min(a[index1],b[index2],c[index3])
        if min == 'A':
            if index1 < len(a)-1:
                index1+=1
            else:
                return a[index1], b[index2], c[index3]
        elif min == 'B':
            if index2 < len(b)-1:
                index2+=1
            else:
                return a[index1], b[index2], c[index3]         
        else:
            if index3 < len(c)-1:
                index3+=1
            else:
                return a[index1], b[index2], c[index3]

def triple_min(a, b, c):
    return 'A' if a < b else 'B' if b < c else 'C'

if __name__ == "__main__":
    print(A,B,C)
    print(search_triple(A, B, C))
