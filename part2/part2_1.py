import sys

s = input().split(' ')
d = {}

def on(s):
    global d
    out = []
    for i in s:
        if i in d.keys():
            d[i] += 1
            if d[i] > len(s)/3 and i not in out:
                out.append(i)
        else:
            d[i] = 1
    return out

#摩尔投票法
def on_v2(s):
    out = []
    candidate1 = s[0]
    candidate2 = s[0]
    cnt1 = 0
    cnt2 = 0
    for i in s:
        if i == candidate1:
            cnt1 += 1
            continue
        if i == candidate2:
            cnt2 += 1
            continue

        if cnt1 == 0:
            candidate1 = i
            cnt1 += 1
            continue
        if cnt2 == 0:
            candidate2 = i
            cnt2 += 1
            continue
        cnt1 -= 1
        cnt2 -= 1

    cnt1 = cnt2 = 0
    for i in s:
        if i == candidate1:
            cnt1 += 1
        elif i == candidate2:
            cnt2 += 1
    if cnt1 > len(s)/3:
        out.append(candidate1)
    if cnt2 > len(s)/3:
        out.append(candidate2)

    return out

print(on(s))
print(on_v2(s))

a = []
a.append(1)
a.append(2)
a.append(3)
print(a)
