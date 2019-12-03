import sys

data = [1,-2,3,10,-4,7,2,-5]

#动态规划，状态转移
def maxseq(seq):
    #状态转移序列
    trans = [0]*len(seq)

    for index, i in enumerate(seq):
        if index == 0:
            trans[index] = seq[0]
            end_index = 0
            maxtrans = seq[0]
        else:
            trans[index] = seq[index] if seq[index] > trans[index-1]+seq[index] else trans[index-1]+seq[index]
            if trans[index] >= maxtrans:
                maxtrans = trans[index]
                end_index = index
    #当最小值为负数时
    if maxtrans <= 0:
        return maxtrans

    start_index = end_index-1
    while trans[start_index] > 0:
        start_index -= 1
    start_index += 1
    
    return seq[start_index:end_index+1], maxtrans


if __name__ == "__main__":
    print(maxseq(data))