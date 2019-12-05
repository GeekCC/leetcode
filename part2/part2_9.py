import sys

data1 = "123431"
data2 = "1234431"

def search(seq):
    if len(seq) == 0:
        return False

    trans = [[False for i in range(len(seq))] for i in range(len(seq))]
    maxlen = 1
    left = 0
    right = 0

    for i in range(len(seq)):
        trans[i][i] = True
        if i < len(seq)-1 and seq[i] == seq[i+1]:
            trans[i][i+1] = True
            maxlen = 2
        
    for seqlenth in range(3, len(seq) + 1):
        for start in range(0, len(seq) - seqlenth + 1):
            end = start + seqlenth - 1
            if trans[start+1][end-1] == True and seq[start] == seq[end]:
                trans[start][end] = True
                if seqlenth > maxlen:
                    left = start
                    right = end
                    maxlen = seqlenth
    return seq[left:right+1]

if __name__ == "__main__":
    print(search(data1))
