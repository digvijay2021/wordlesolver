from words import *


def getTop2(arr):
    tw1 = ()
    tw2 = ()
    for k,i in zip(arr,range(len(arr))):
        # print(tw1)
        # print(tw2)
        # print("<------------------>")

        if not tw1:
            tw1 = (i, k)
            continue

        if not tw2:
            tw2 = (i, k)
            continue
        
        if tw2[1] > tw1[1]:
            tw1, tw2 = tw2, tw1

        
        if k > tw1[1]:
            tw1 = (i, k)
            continue

        if k > tw2[1]:
            tw2 = (i, k)
            continue
    tw1 = (chr(tw1[0] + 65), tw1[1])
    tw2 = (chr(tw2[0] + 65), tw2[1])
    return [tw1, tw2]
        


def windex(a):
    return ord(a) - 97

rows, cols = (5, 26)
chararr = [[0 for i in range(cols)] for j in range(rows)]
foarr = [[0 for i in range(cols)] for j in range(rows)]

for word in wordles:
    for i,k in enumerate(word):
        chararr[i][windex(k)] += 1
    # print(chararr)

for word in fo:
    for i,k in enumerate(word):
        foarr[i][windex(k)] += 1

topwords = []
for pos in chararr:
    topwords.append(getTop2(pos))

print(topwords)



winwords = []

noindarr = []
for i in range(26):
    noindarr.append(0)
    for j in range(5):
        noindarr[i] += chararr[j][i]

wc = []
for k,i in zip(noindarr, range(26)):
    wc.append((chr(i + 65), k))

noindarr.sort(reverse=True)
print(wc)
print(noindarr)




