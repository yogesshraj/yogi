ascendingorder.py

l = [64, -25, 12, 22, 11, 1,2,44,3,122, 23, 34]

for i in range(len(l)):
    for j in range(i + 1, len(l)):

        if l[i] > l[j]:
           l[i], l[j] = l[j], l[i]

print (l)




#ascending order with only one loop

s = [-5, -23, 5, 0, 23, -6, 23, 67]
nl = []
for i in range(len(s)):
    a = min(s)
    nl.append(a)
    s.remove(a)

print (nl)