dic={1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
for x in dic:
    for y in dic:
        if dic[x]>dic[y]:
            dic[x],dic[y]=dic[y],dic[x]
print(dic)
