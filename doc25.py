word="w3resource"
i=0
d={}
while i<len(word):
    j=0
    c=0
    while j<len(word):
        if word[i]==word[j]:
            c=c+1
        d[word[i]]=c
        j=j+1
    i=i+1
print(d)
